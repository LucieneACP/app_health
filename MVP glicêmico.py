{
	"cells": [
		{
			"id": "68fb8ceb1f8468750b27638e",
			"cell_type": "code",
			"source": "# Notebook Enxuto – MVP Saúde\nimport pandas as pd\nimport numpy as np\nimport plotly.express as px\nfrom datetime import datetime, date\n\n# -----------------------\n# 1. Dados simulados iniciais\n# -----------------------\nnp.random.seed(42)\ndias = pd.date_range(start=\"2025-10-01\", periods=10, freq='D')\nglicemia = np.random.randint(60, 220, size=len(dias))\ncarboidratos = np.random.randint(0, 150, size=len(dias))\nagua = np.random.choice([\"Sim\", \"Não\"], size=len(dias))\natividade = np.random.choice([\"Sim\", \"Não\"], size=len(dias))\nmedicacao = np.random.choice([\"Tomou\", \"Não tomou\"], size=len(dias))\n\ndf = pd.DataFrame({\n    \"Data\": dias,\n    \"Glicemia (mg/dL)\": glicemia,\n    \"Carboidratos (g)\": carboidratos,\n    \"Água\": agua,\n    \"Atividade Física\": atividade,\n    \"Medicação\": medicacao\n})\n\n# -----------------------\n# 2. Função para atualizar métricas\n# -----------------------\ndef atualizar_metricas(df):\n    df[\"Risco Hipoglicemia\"] = df[\"Glicemia (mg/dL)\"] < 70\n    df[\"Risco Hiperglicemia\"] = df[\"Glicemia (mg/dL)\"] > 180\n    df[\"Adesão (%)\"] = df[\"Medicação\"].apply(lambda x: 100 if x==\"Tomou\" else 0)\n    return df\n\ndf = atualizar_metricas(df)\n\n# -----------------------\n# 3. Função para registro manual\n# -----------------------\ndef adicionar_registro_manual():\n    print(\"\\n--- Inserir novo registro ---\")\n    try:\n        data_str = input(\"Data (AAAA-MM-DD): \")\n        data = datetime.strptime(data_str, \"%Y-%m-%d\")\n    except:\n        data = date.today()\n    glicemia_val = float(input(\"Glicemia (mg/dL): \"))\n    carbo_val = float(input(\"Carboidratos (g): \"))\n    agua_val = input(\"Tomou água? (Sim/Não): \")\n    atividade_val = input(\"Fez atividade física? (Sim/Não): \")\n    medicacao_val = input(\"Tomou medicação? (Tomou/Não tomou): \")\n    \n    novo = pd.DataFrame([{\n        \"Data\": data,\n        \"Glicemia (mg/dL)\": glicemia_val,\n        \"Carboidratos (g)\": carbo_val,\n        \"Água\": agua_val,\n        \"Atividade Física\": atividade_val,\n        \"Medicação\": medicacao_val\n    }])\n    global df\n    df = pd.concat([df, novo], ignore_index=True)\n    df = atualizar_metricas(df)\n    print(\"✅ Registro adicionado!\\n\")\n\n# -----------------------\n# 4. Visualizações\n# -----------------------\ndef mostrar_graficos(df):\n    # Glicemia\n    px.line(df, x=\"Data\", y=\"Glicemia (mg/dL)\", markers=True, title=\"Distribuição de Glicemia\").show()\n    \n    # Carboidratos\n    px.bar(df, x=\"Data\", y=\"Carboidratos (g)\", title=\"Ingestão de Carboidratos\").show()\n    \n    # Água e atividade física\n    df_habitos = df.melt(id_vars=\"Data\", value_vars=[\"Água\", \"Atividade Física\"])\n    px.bar(df_habitos, x=\"Data\", y=\"value\", color=\"variable\", barmode=\"group\", title=\"Hidratação e Atividade Física\").show()\n    \n    # Riscos Hipo/Hiper\n    px.scatter(\n        df,\n        x=\"Data\",\n        y=\"Glicemia (mg/dL)\",\n        color=df[\"Risco Hipoglicemia\"].map({True: \"Hipo\", False: \"Normal\"}),\n        symbol=df[\"Risco Hiperglicemia\"].map({True: \"Hiper\", False: \"Normal\"}),\n        title=\"Risco de Hipo/Hiperglicemia\"\n    ).show()\n    \n    # Adesão à medicação\n    px.bar(df, x=\"Data\", y=\"Adesão (%)\", title=\"Adesão à Medicação\").show()\n\n# -----------------------\n# 5. Execução inicial\n# -----------------------\nprint(\"📊 Dados simulados iniciais:\")\ndisplay(df)\nmostrar_graficos(df)\n\n# -----------------------\n# 6. Inserir registros manuais\n# -----------------------\nwhile True:\n    resp = input(\"Deseja adicionar registro manual? (Sim/Não): \").strip().lower()\n    if resp == \"sim\":\n        adicionar_registro_manual()\n        mostrar_graficos(df)\n        display(df)\n    else:\n        print(\"✅ Sessão finalizada.\")\n        break\n",
			"metadata": {
				"name": "First cell",
				"collapsed": true,
				"scrolled": "auto",
				"datarobot": {
					"language": "python"
				},
				"hide_code": false,
				"hide_results": false,
				"disable_run": false,
				"chart_settings": null,
				"custom_metric_settings": null,
				"custom_llm_metric_settings": null,
				"dataframe_view_options": null
			},
			"outputs": [
				{
					"output_type": "execute_result",
					"execution_count": 6,
					"data": {
						"text/plain": "📊 Dados simulados iniciais:\n"
					},
					"metadata": {}
				},
				{
					"output_type": "execute_result",
					"execution_count": 6,
					"data": {
						"text/plain": "        Data  Glicemia (mg/dL)  Carboidratos (g) Água Atividade Física  \\\n0 2025-10-01               162               116  Não              Sim   \n1 2025-10-02               152                99  Não              Sim   \n2 2025-10-03                74               103  Sim              Sim   \n3 2025-10-04               166               130  Sim              Sim   \n4 2025-10-05               131               149  Não              Não   \n5 2025-10-06                80                52  Não              Não   \n6 2025-10-07               162                 1  Não              Não   \n7 2025-10-08               181                87  Sim              Não   \n8 2025-10-09               134                37  Não              Não   \n9 2025-10-10               147               129  Sim              Sim   \n\n   Medicação  Risco Hipoglicemia  Risco Hiperglicemia  Adesão (%)  \n0  Não tomou               False                False           0  \n1  Não tomou               False                False           0  \n2      Tomou               False                False         100  \n3  Não tomou               False                False           0  \n4      Tomou               False                False         100  \n5  Não tomou               False                False           0  \n6      Tomou               False                False         100  \n7  Não tomou               False                 True           0  \n8  Não tomou               False                False           0  \n9      Tomou               False                False         100  ",
						"text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Data</th>\n      <th>Glicemia (mg/dL)</th>\n      <th>Carboidratos (g)</th>\n      <th>Água</th>\n      <th>Atividade Física</th>\n      <th>Medicação</th>\n      <th>Risco Hipoglicemia</th>\n      <th>Risco Hiperglicemia</th>\n      <th>Adesão (%)</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>2025-10-01</td>\n      <td>162</td>\n      <td>116</td>\n      <td>Não</td>\n      <td>Sim</td>\n      <td>Não tomou</td>\n      <td>False</td>\n      <td>False</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>2025-10-02</td>\n      <td>152</td>\n      <td>99</td>\n      <td>Não</td>\n      <td>Sim</td>\n      <td>Não tomou</td>\n      <td>False</td>\n      <td>False</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>2025-10-03</td>\n      <td>74</td>\n      <td>103</td>\n      <td>Sim</td>\n      <td>Sim</td>\n      <td>Tomou</td>\n      <td>False</td>\n      <td>False</td>\n      <td>100</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>2025-10-04</td>\n      <td>166</td>\n      <td>130</td>\n      <td>Sim</td>\n      <td>Sim</td>\n      <td>Não tomou</td>\n      <td>False</td>\n      <td>False</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>2025-10-05</td>\n      <td>131</td>\n      <td>149</td>\n      <td>Não</td>\n      <td>Não</td>\n      <td>Tomou</td>\n      <td>False</td>\n      <td>False</td>\n      <td>100</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>2025-10-06</td>\n      <td>80</td>\n      <td>52</td>\n      <td>Não</td>\n      <td>Não</td>\n      <td>Não tomou</td>\n      <td>False</td>\n      <td>False</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>2025-10-07</td>\n      <td>162</td>\n      <td>1</td>\n      <td>Não</td>\n      <td>Não</td>\n      <td>Tomou</td>\n      <td>False</td>\n      <td>False</td>\n      <td>100</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>2025-10-08</td>\n      <td>181</td>\n      <td>87</td>\n      <td>Sim</td>\n      <td>Não</td>\n      <td>Não tomou</td>\n      <td>False</td>\n      <td>True</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>2025-10-09</td>\n      <td>134</td>\n      <td>37</td>\n      <td>Não</td>\n      <td>Não</td>\n      <td>Não tomou</td>\n      <td>False</td>\n      <td>False</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>2025-10-10</td>\n      <td>147</td>\n      <td>129</td>\n      <td>Sim</td>\n      <td>Sim</td>\n      <td>Tomou</td>\n      <td>False</td>\n      <td>False</td>\n      <td>100</td>\n    </tr>\n  </tbody>\n</table>\n</div>",
						"application/vnd.dataframe+json": {
							"data": [
								{
									"index": 0,
									"Data": "2025-10-01T00:00:00.000",
									"Glicemia (mg/dL)": 162,
									"Carboidratos (g)": 116,
									"Água": "Não",
									"Atividade Física": "Sim",
									"Medicação": "Não tomou",
									"Risco Hipoglicemia": false,
									"Risco Hiperglicemia": false,
									"Adesão (%)": 0
								},
								{
									"index": 1,
									"Data": "2025-10-02T00:00:00.000",
									"Glicemia (mg/dL)": 152,
									"Carboidratos (g)": 99,
									"Água": "Não",
									"Atividade Física": "Sim",
									"Medicação": "Não tomou",
									"Risco Hipoglicemia": false,
									"Risco Hiperglicemia": false,
									"Adesão (%)": 0
								},
								{
									"index": 2,
									"Data": "2025-10-03T00:00:00.000",
									"Glicemia (mg/dL)": 74,
									"Carboidratos (g)": 103,
									"Água": "Sim",
									"Atividade Física": "Sim",
									"Medicação": "Tomou",
									"Risco Hipoglicemia": false,
									"Risco Hiperglicemia": false,
									"Adesão (%)": 100
								},
								{
									"index": 3,
									"Data": "2025-10-04T00:00:00.000",
									"Glicemia (mg/dL)": 166,
									"Carboidratos (g)": 130,
									"Água": "Sim",
									"Atividade Física": "Sim",
									"Medicação": "Não tomou",
									"Risco Hipoglicemia": false,
									"Risco Hiperglicemia": false,
									"Adesão (%)": 0
								},
								{
									"index": 4,
									"Data": "2025-10-05T00:00:00.000",
									"Glicemia (mg/dL)": 131,
									"Carboidratos (g)": 149,
									"Água": "Não",
									"Atividade Física": "Não",
									"Medicação": "Tomou",
									"Risco Hipoglicemia": false,
									"Risco Hiperglicemia": false,
									"Adesão (%)": 100
								},
								{
									"index": 5,
									"Data": "2025-10-06T00:00:00.000",
									"Glicemia (mg/dL)": 80,
									"Carboidratos (g)": 52,
									"Água": "Não",
									"Atividade Física": "Não",
									"Medicação": "Não tomou",
									"Risco Hipoglicemia": false,
									"Risco Hiperglicemia": false,
									"Adesão (%)": 0
								},
								{
									"index": 6,
									"Data": "2025-10-07T00:00:00.000",
									"Glicemia (mg/dL)": 162,
									"Carboidratos (g)": 1,
									"Água": "Não",
									"Atividade Física": "Não",
									"Medicação": "Tomou",
									"Risco Hipoglicemia": false,
									"Risco Hiperglicemia": false,
									"Adesão (%)": 100
								},
								{
									"index": 7,
									"Data": "2025-10-08T00:00:00.000",
									"Glicemia (mg/dL)": 181,
									"Carboidratos (g)": 87,
									"Água": "Sim",
									"Atividade Física": "Não",
									"Medicação": "Não tomou",
									"Risco Hipoglicemia": false,
									"Risco Hiperglicemia": true,
									"Adesão (%)": 0
								},
								{
									"index": 8,
									"Data": "2025-10-09T00:00:00.000",
									"Glicemia (mg/dL)": 134,
									"Carboidratos (g)": 37,
									"Água": "Não",
									"Atividade Física": "Não",
									"Medicação": "Não tomou",
									"Risco Hipoglicemia": false,
									"Risco Hiperglicemia": false,
									"Adesão (%)": 0
								},
								{
									"index": 9,
									"Data": "2025-10-10T00:00:00.000",
									"Glicemia (mg/dL)": 147,
									"Carboidratos (g)": 129,
									"Água": "Sim",
									"Atividade Física": "Sim",
									"Medicação": "Tomou",
									"Risco Hipoglicemia": false,
									"Risco Hiperglicemia": false,
									"Adesão (%)": 100
								}
							],
							"columns": [
								{
									"name": "index",
									"type": "integer"
								},
								{
									"name": "Data",
									"type": "datetime"
								},
								{
									"name": "Glicemia (mg/dL)",
									"type": "integer"
								},
								{
									"name": "Carboidratos (g)",
									"type": "integer"
								},
								{
									"name": "Água",
									"type": "string"
								},
								{
									"name": "Atividade Física",
									"type": "string"
								},
								{
									"name": "Medicação",
									"type": "string"
								},
								{
									"name": "Risco Hipoglicemia",
									"type": "boolean"
								},
								{
									"name": "Risco Hiperglicemia",
									"type": "boolean"
								},
								{
									"name": "Adesão (%)",
									"type": "integer"
								}
							],
							"count": 10,
							"totalCount": 10,
							"offset": 0,
							"limit": 10,
							"referenceId": 140688949582352,
							"sortedBy": "",
							"indexKey": "index",
							"error": []
						}
					},
					"metadata": {}
				},
				{
					"output_type": "execute_result",
					"execution_count": 6,
					"data": {
						"application/vnd.plotly.v1+json": {
							"data": [
								{
									"hovertemplate": "Data=%{x}<br>Glicemia (mg/dL)=%{y}<extra></extra>",
									"legendgroup": "",
									"line": {
										"color": "#636efa",
										"dash": "solid"
									},
									"marker": {
										"symbol": "circle"
									},
									"mode": "lines+markers",
									"name": "",
									"orientation": "v",
									"showlegend": false,
									"x": [
										"2025-10-01T00:00:00",
										"2025-10-02T00:00:00",
										"2025-10-03T00:00:00",
										"2025-10-04T00:00:00",
										"2025-10-05T00:00:00",
										"2025-10-06T00:00:00",
										"2025-10-07T00:00:00",
										"2025-10-08T00:00:00",
										"2025-10-09T00:00:00",
										"2025-10-10T00:00:00"
									],
									"xaxis": "x",
									"y": [
										162,
										152,
										74,
										166,
										131,
										80,
										162,
										181,
										134,
										147
									],
									"yaxis": "y",
									"type": "scatter"
								}
							],
							"layout": {
								"template": {
									"data": {
										"histogram2dcontour": [
											{
												"type": "histogram2dcontour",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"choropleth": [
											{
												"type": "choropleth",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"histogram2d": [
											{
												"type": "histogram2d",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"heatmap": [
											{
												"type": "heatmap",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"heatmapgl": [
											{
												"type": "heatmapgl",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"contourcarpet": [
											{
												"type": "contourcarpet",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"contour": [
											{
												"type": "contour",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"surface": [
											{
												"type": "surface",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"mesh3d": [
											{
												"type": "mesh3d",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"scatter": [
											{
												"fillpattern": {
													"fillmode": "overlay",
													"size": 10,
													"solidity": 0.2
												},
												"type": "scatter"
											}
										],
										"parcoords": [
											{
												"type": "parcoords",
												"line": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterpolargl": [
											{
												"type": "scatterpolargl",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"bar": [
											{
												"error_x": {
													"color": "#2a3f5f"
												},
												"error_y": {
													"color": "#2a3f5f"
												},
												"marker": {
													"line": {
														"color": "#E5ECF6",
														"width": 0.5
													},
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "bar"
											}
										],
										"scattergeo": [
											{
												"type": "scattergeo",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterpolar": [
											{
												"type": "scatterpolar",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"histogram": [
											{
												"marker": {
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "histogram"
											}
										],
										"scattergl": [
											{
												"type": "scattergl",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatter3d": [
											{
												"type": "scatter3d",
												"line": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												},
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scattermapbox": [
											{
												"type": "scattermapbox",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterternary": [
											{
												"type": "scatterternary",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scattercarpet": [
											{
												"type": "scattercarpet",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"carpet": [
											{
												"aaxis": {
													"endlinecolor": "#2a3f5f",
													"gridcolor": "white",
													"linecolor": "white",
													"minorgridcolor": "white",
													"startlinecolor": "#2a3f5f"
												},
												"baxis": {
													"endlinecolor": "#2a3f5f",
													"gridcolor": "white",
													"linecolor": "white",
													"minorgridcolor": "white",
													"startlinecolor": "#2a3f5f"
												},
												"type": "carpet"
											}
										],
										"table": [
											{
												"cells": {
													"fill": {
														"color": "#EBF0F8"
													},
													"line": {
														"color": "white"
													}
												},
												"header": {
													"fill": {
														"color": "#C8D4E3"
													},
													"line": {
														"color": "white"
													}
												},
												"type": "table"
											}
										],
										"barpolar": [
											{
												"marker": {
													"line": {
														"color": "#E5ECF6",
														"width": 0.5
													},
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "barpolar"
											}
										],
										"pie": [
											{
												"automargin": true,
												"type": "pie"
											}
										]
									},
									"layout": {
										"autotypenumbers": "strict",
										"colorway": [
											"#636efa",
											"#EF553B",
											"#00cc96",
											"#ab63fa",
											"#FFA15A",
											"#19d3f3",
											"#FF6692",
											"#B6E880",
											"#FF97FF",
											"#FECB52"
										],
										"font": {
											"color": "#2a3f5f"
										},
										"hovermode": "closest",
										"hoverlabel": {
											"align": "left"
										},
										"paper_bgcolor": "white",
										"plot_bgcolor": "#E5ECF6",
										"polar": {
											"bgcolor": "#E5ECF6",
											"angularaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"radialaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											}
										},
										"ternary": {
											"bgcolor": "#E5ECF6",
											"aaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"baxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"caxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											}
										},
										"coloraxis": {
											"colorbar": {
												"outlinewidth": 0,
												"ticks": ""
											}
										},
										"colorscale": {
											"sequential": [
												[
													0,
													"#0d0887"
												],
												[
													0.1111111111111111,
													"#46039f"
												],
												[
													0.2222222222222222,
													"#7201a8"
												],
												[
													0.3333333333333333,
													"#9c179e"
												],
												[
													0.4444444444444444,
													"#bd3786"
												],
												[
													0.5555555555555556,
													"#d8576b"
												],
												[
													0.6666666666666666,
													"#ed7953"
												],
												[
													0.7777777777777778,
													"#fb9f3a"
												],
												[
													0.8888888888888888,
													"#fdca26"
												],
												[
													1,
													"#f0f921"
												]
											],
											"sequentialminus": [
												[
													0,
													"#0d0887"
												],
												[
													0.1111111111111111,
													"#46039f"
												],
												[
													0.2222222222222222,
													"#7201a8"
												],
												[
													0.3333333333333333,
													"#9c179e"
												],
												[
													0.4444444444444444,
													"#bd3786"
												],
												[
													0.5555555555555556,
													"#d8576b"
												],
												[
													0.6666666666666666,
													"#ed7953"
												],
												[
													0.7777777777777778,
													"#fb9f3a"
												],
												[
													0.8888888888888888,
													"#fdca26"
												],
												[
													1,
													"#f0f921"
												]
											],
											"diverging": [
												[
													0,
													"#8e0152"
												],
												[
													0.1,
													"#c51b7d"
												],
												[
													0.2,
													"#de77ae"
												],
												[
													0.3,
													"#f1b6da"
												],
												[
													0.4,
													"#fde0ef"
												],
												[
													0.5,
													"#f7f7f7"
												],
												[
													0.6,
													"#e6f5d0"
												],
												[
													0.7,
													"#b8e186"
												],
												[
													0.8,
													"#7fbc41"
												],
												[
													0.9,
													"#4d9221"
												],
												[
													1,
													"#276419"
												]
											]
										},
										"xaxis": {
											"gridcolor": "white",
											"linecolor": "white",
											"ticks": "",
											"title": {
												"standoff": 15
											},
											"zerolinecolor": "white",
											"automargin": true,
											"zerolinewidth": 2
										},
										"yaxis": {
											"gridcolor": "white",
											"linecolor": "white",
											"ticks": "",
											"title": {
												"standoff": 15
											},
											"zerolinecolor": "white",
											"automargin": true,
											"zerolinewidth": 2
										},
										"scene": {
											"xaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											},
											"yaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											},
											"zaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											}
										},
										"shapedefaults": {
											"line": {
												"color": "#2a3f5f"
											}
										},
										"annotationdefaults": {
											"arrowcolor": "#2a3f5f",
											"arrowhead": 0,
											"arrowwidth": 1
										},
										"geo": {
											"bgcolor": "white",
											"landcolor": "#E5ECF6",
											"subunitcolor": "white",
											"showland": true,
											"showlakes": true,
											"lakecolor": "white"
										},
										"title": {
											"x": 0.05
										},
										"mapbox": {
											"style": "light"
										}
									}
								},
								"xaxis": {
									"anchor": "y",
									"domain": [
										0,
										1
									],
									"title": {
										"text": "Data"
									}
								},
								"yaxis": {
									"anchor": "x",
									"domain": [
										0,
										1
									],
									"title": {
										"text": "Glicemia (mg/dL)"
									}
								},
								"legend": {
									"tracegroupgap": 0
								},
								"title": {
									"text": "Distribuição de Glicemia"
								}
							},
							"config": {
								"plotlyServerURL": "https://plot.ly"
							}
						},
						"text/html": "<div>                            <div id=\"aa1b892d-0971-4f56-a40d-84d0c0fc2adc\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"aa1b892d-0971-4f56-a40d-84d0c0fc2adc\")) {                    Plotly.newPlot(                        \"aa1b892d-0971-4f56-a40d-84d0c0fc2adc\",                        [{\"hovertemplate\":\"Data=%{x}\\u003cbr\\u003eGlicemia (mg\\u002fdL)=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines+markers\",\"name\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x\":[\"2025-10-01T00:00:00\",\"2025-10-02T00:00:00\",\"2025-10-03T00:00:00\",\"2025-10-04T00:00:00\",\"2025-10-05T00:00:00\",\"2025-10-06T00:00:00\",\"2025-10-07T00:00:00\",\"2025-10-08T00:00:00\",\"2025-10-09T00:00:00\",\"2025-10-10T00:00:00\"],\"xaxis\":\"x\",\"y\":[162,152,74,166,131,80,162,181,134,147],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Data\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Glicemia (mg\\u002fdL)\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Distribuição de Glicemia\"}},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('aa1b892d-0971-4f56-a40d-84d0c0fc2adc');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
					},
					"metadata": {}
				},
				{
					"output_type": "execute_result",
					"execution_count": 6,
					"data": {
						"application/vnd.plotly.v1+json": {
							"data": [
								{
									"alignmentgroup": "True",
									"hovertemplate": "Data=%{x}<br>Carboidratos (g)=%{y}<extra></extra>",
									"legendgroup": "",
									"marker": {
										"color": "#636efa",
										"pattern": {
											"shape": ""
										}
									},
									"name": "",
									"offsetgroup": "",
									"orientation": "v",
									"showlegend": false,
									"textposition": "auto",
									"x": [
										"2025-10-01T00:00:00",
										"2025-10-02T00:00:00",
										"2025-10-03T00:00:00",
										"2025-10-04T00:00:00",
										"2025-10-05T00:00:00",
										"2025-10-06T00:00:00",
										"2025-10-07T00:00:00",
										"2025-10-08T00:00:00",
										"2025-10-09T00:00:00",
										"2025-10-10T00:00:00"
									],
									"xaxis": "x",
									"y": [
										116,
										99,
										103,
										130,
										149,
										52,
										1,
										87,
										37,
										129
									],
									"yaxis": "y",
									"type": "bar"
								}
							],
							"layout": {
								"template": {
									"data": {
										"histogram2dcontour": [
											{
												"type": "histogram2dcontour",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"choropleth": [
											{
												"type": "choropleth",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"histogram2d": [
											{
												"type": "histogram2d",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"heatmap": [
											{
												"type": "heatmap",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"heatmapgl": [
											{
												"type": "heatmapgl",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"contourcarpet": [
											{
												"type": "contourcarpet",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"contour": [
											{
												"type": "contour",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"surface": [
											{
												"type": "surface",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"mesh3d": [
											{
												"type": "mesh3d",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"scatter": [
											{
												"fillpattern": {
													"fillmode": "overlay",
													"size": 10,
													"solidity": 0.2
												},
												"type": "scatter"
											}
										],
										"parcoords": [
											{
												"type": "parcoords",
												"line": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterpolargl": [
											{
												"type": "scatterpolargl",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"bar": [
											{
												"error_x": {
													"color": "#2a3f5f"
												},
												"error_y": {
													"color": "#2a3f5f"
												},
												"marker": {
													"line": {
														"color": "#E5ECF6",
														"width": 0.5
													},
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "bar"
											}
										],
										"scattergeo": [
											{
												"type": "scattergeo",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterpolar": [
											{
												"type": "scatterpolar",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"histogram": [
											{
												"marker": {
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "histogram"
											}
										],
										"scattergl": [
											{
												"type": "scattergl",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatter3d": [
											{
												"type": "scatter3d",
												"line": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												},
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scattermapbox": [
											{
												"type": "scattermapbox",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterternary": [
											{
												"type": "scatterternary",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scattercarpet": [
											{
												"type": "scattercarpet",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"carpet": [
											{
												"aaxis": {
													"endlinecolor": "#2a3f5f",
													"gridcolor": "white",
													"linecolor": "white",
													"minorgridcolor": "white",
													"startlinecolor": "#2a3f5f"
												},
												"baxis": {
													"endlinecolor": "#2a3f5f",
													"gridcolor": "white",
													"linecolor": "white",
													"minorgridcolor": "white",
													"startlinecolor": "#2a3f5f"
												},
												"type": "carpet"
											}
										],
										"table": [
											{
												"cells": {
													"fill": {
														"color": "#EBF0F8"
													},
													"line": {
														"color": "white"
													}
												},
												"header": {
													"fill": {
														"color": "#C8D4E3"
													},
													"line": {
														"color": "white"
													}
												},
												"type": "table"
											}
										],
										"barpolar": [
											{
												"marker": {
													"line": {
														"color": "#E5ECF6",
														"width": 0.5
													},
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "barpolar"
											}
										],
										"pie": [
											{
												"automargin": true,
												"type": "pie"
											}
										]
									},
									"layout": {
										"autotypenumbers": "strict",
										"colorway": [
											"#636efa",
											"#EF553B",
											"#00cc96",
											"#ab63fa",
											"#FFA15A",
											"#19d3f3",
											"#FF6692",
											"#B6E880",
											"#FF97FF",
											"#FECB52"
										],
										"font": {
											"color": "#2a3f5f"
										},
										"hovermode": "closest",
										"hoverlabel": {
											"align": "left"
										},
										"paper_bgcolor": "white",
										"plot_bgcolor": "#E5ECF6",
										"polar": {
											"bgcolor": "#E5ECF6",
											"angularaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"radialaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											}
										},
										"ternary": {
											"bgcolor": "#E5ECF6",
											"aaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"baxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"caxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											}
										},
										"coloraxis": {
											"colorbar": {
												"outlinewidth": 0,
												"ticks": ""
											}
										},
										"colorscale": {
											"sequential": [
												[
													0,
													"#0d0887"
												],
												[
													0.1111111111111111,
													"#46039f"
												],
												[
													0.2222222222222222,
													"#7201a8"
												],
												[
													0.3333333333333333,
													"#9c179e"
												],
												[
													0.4444444444444444,
													"#bd3786"
												],
												[
													0.5555555555555556,
													"#d8576b"
												],
												[
													0.6666666666666666,
													"#ed7953"
												],
												[
													0.7777777777777778,
													"#fb9f3a"
												],
												[
													0.8888888888888888,
													"#fdca26"
												],
												[
													1,
													"#f0f921"
												]
											],
											"sequentialminus": [
												[
													0,
													"#0d0887"
												],
												[
													0.1111111111111111,
													"#46039f"
												],
												[
													0.2222222222222222,
													"#7201a8"
												],
												[
													0.3333333333333333,
													"#9c179e"
												],
												[
													0.4444444444444444,
													"#bd3786"
												],
												[
													0.5555555555555556,
													"#d8576b"
												],
												[
													0.6666666666666666,
													"#ed7953"
												],
												[
													0.7777777777777778,
													"#fb9f3a"
												],
												[
													0.8888888888888888,
													"#fdca26"
												],
												[
													1,
													"#f0f921"
												]
											],
											"diverging": [
												[
													0,
													"#8e0152"
												],
												[
													0.1,
													"#c51b7d"
												],
												[
													0.2,
													"#de77ae"
												],
												[
													0.3,
													"#f1b6da"
												],
												[
													0.4,
													"#fde0ef"
												],
												[
													0.5,
													"#f7f7f7"
												],
												[
													0.6,
													"#e6f5d0"
												],
												[
													0.7,
													"#b8e186"
												],
												[
													0.8,
													"#7fbc41"
												],
												[
													0.9,
													"#4d9221"
												],
												[
													1,
													"#276419"
												]
											]
										},
										"xaxis": {
											"gridcolor": "white",
											"linecolor": "white",
											"ticks": "",
											"title": {
												"standoff": 15
											},
											"zerolinecolor": "white",
											"automargin": true,
											"zerolinewidth": 2
										},
										"yaxis": {
											"gridcolor": "white",
											"linecolor": "white",
											"ticks": "",
											"title": {
												"standoff": 15
											},
											"zerolinecolor": "white",
											"automargin": true,
											"zerolinewidth": 2
										},
										"scene": {
											"xaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											},
											"yaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											},
											"zaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											}
										},
										"shapedefaults": {
											"line": {
												"color": "#2a3f5f"
											}
										},
										"annotationdefaults": {
											"arrowcolor": "#2a3f5f",
											"arrowhead": 0,
											"arrowwidth": 1
										},
										"geo": {
											"bgcolor": "white",
											"landcolor": "#E5ECF6",
											"subunitcolor": "white",
											"showland": true,
											"showlakes": true,
											"lakecolor": "white"
										},
										"title": {
											"x": 0.05
										},
										"mapbox": {
											"style": "light"
										}
									}
								},
								"xaxis": {
									"anchor": "y",
									"domain": [
										0,
										1
									],
									"title": {
										"text": "Data"
									}
								},
								"yaxis": {
									"anchor": "x",
									"domain": [
										0,
										1
									],
									"title": {
										"text": "Carboidratos (g)"
									}
								},
								"legend": {
									"tracegroupgap": 0
								},
								"title": {
									"text": "Ingestão de Carboidratos"
								},
								"barmode": "relative"
							},
							"config": {
								"plotlyServerURL": "https://plot.ly"
							}
						},
						"text/html": "<div>                            <div id=\"bd050b85-9615-4773-a9d1-156bebdce7d5\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"bd050b85-9615-4773-a9d1-156bebdce7d5\")) {                    Plotly.newPlot(                        \"bd050b85-9615-4773-a9d1-156bebdce7d5\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"Data=%{x}\\u003cbr\\u003eCarboidratos (g)=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"2025-10-01T00:00:00\",\"2025-10-02T00:00:00\",\"2025-10-03T00:00:00\",\"2025-10-04T00:00:00\",\"2025-10-05T00:00:00\",\"2025-10-06T00:00:00\",\"2025-10-07T00:00:00\",\"2025-10-08T00:00:00\",\"2025-10-09T00:00:00\",\"2025-10-10T00:00:00\"],\"xaxis\":\"x\",\"y\":[116,99,103,130,149,52,1,87,37,129],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Data\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Carboidratos (g)\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Ingestão de Carboidratos\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('bd050b85-9615-4773-a9d1-156bebdce7d5');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
					},
					"metadata": {}
				},
				{
					"output_type": "execute_result",
					"execution_count": 6,
					"data": {
						"application/vnd.plotly.v1+json": {
							"data": [
								{
									"alignmentgroup": "True",
									"hovertemplate": "variable=Água<br>Data=%{x}<br>value=%{y}<extra></extra>",
									"legendgroup": "Água",
									"marker": {
										"color": "#636efa",
										"pattern": {
											"shape": ""
										}
									},
									"name": "Água",
									"offsetgroup": "Água",
									"orientation": "v",
									"showlegend": true,
									"textposition": "auto",
									"x": [
										"2025-10-01T00:00:00",
										"2025-10-02T00:00:00",
										"2025-10-03T00:00:00",
										"2025-10-04T00:00:00",
										"2025-10-05T00:00:00",
										"2025-10-06T00:00:00",
										"2025-10-07T00:00:00",
										"2025-10-08T00:00:00",
										"2025-10-09T00:00:00",
										"2025-10-10T00:00:00"
									],
									"xaxis": "x",
									"y": [
										"Não",
										"Não",
										"Sim",
										"Sim",
										"Não",
										"Não",
										"Não",
										"Sim",
										"Não",
										"Sim"
									],
									"yaxis": "y",
									"type": "bar"
								},
								{
									"alignmentgroup": "True",
									"hovertemplate": "variable=Atividade Física<br>Data=%{x}<br>value=%{y}<extra></extra>",
									"legendgroup": "Atividade Física",
									"marker": {
										"color": "#EF553B",
										"pattern": {
											"shape": ""
										}
									},
									"name": "Atividade Física",
									"offsetgroup": "Atividade Física",
									"orientation": "v",
									"showlegend": true,
									"textposition": "auto",
									"x": [
										"2025-10-01T00:00:00",
										"2025-10-02T00:00:00",
										"2025-10-03T00:00:00",
										"2025-10-04T00:00:00",
										"2025-10-05T00:00:00",
										"2025-10-06T00:00:00",
										"2025-10-07T00:00:00",
										"2025-10-08T00:00:00",
										"2025-10-09T00:00:00",
										"2025-10-10T00:00:00"
									],
									"xaxis": "x",
									"y": [
										"Sim",
										"Sim",
										"Sim",
										"Sim",
										"Não",
										"Não",
										"Não",
										"Não",
										"Não",
										"Sim"
									],
									"yaxis": "y",
									"type": "bar"
								}
							],
							"layout": {
								"template": {
									"data": {
										"histogram2dcontour": [
											{
												"type": "histogram2dcontour",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"choropleth": [
											{
												"type": "choropleth",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"histogram2d": [
											{
												"type": "histogram2d",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"heatmap": [
											{
												"type": "heatmap",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"heatmapgl": [
											{
												"type": "heatmapgl",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"contourcarpet": [
											{
												"type": "contourcarpet",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"contour": [
											{
												"type": "contour",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"surface": [
											{
												"type": "surface",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"mesh3d": [
											{
												"type": "mesh3d",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"scatter": [
											{
												"fillpattern": {
													"fillmode": "overlay",
													"size": 10,
													"solidity": 0.2
												},
												"type": "scatter"
											}
										],
										"parcoords": [
											{
												"type": "parcoords",
												"line": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterpolargl": [
											{
												"type": "scatterpolargl",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"bar": [
											{
												"error_x": {
													"color": "#2a3f5f"
												},
												"error_y": {
													"color": "#2a3f5f"
												},
												"marker": {
													"line": {
														"color": "#E5ECF6",
														"width": 0.5
													},
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "bar"
											}
										],
										"scattergeo": [
											{
												"type": "scattergeo",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterpolar": [
											{
												"type": "scatterpolar",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"histogram": [
											{
												"marker": {
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "histogram"
											}
										],
										"scattergl": [
											{
												"type": "scattergl",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatter3d": [
											{
												"type": "scatter3d",
												"line": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												},
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scattermapbox": [
											{
												"type": "scattermapbox",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterternary": [
											{
												"type": "scatterternary",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scattercarpet": [
											{
												"type": "scattercarpet",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"carpet": [
											{
												"aaxis": {
													"endlinecolor": "#2a3f5f",
													"gridcolor": "white",
													"linecolor": "white",
													"minorgridcolor": "white",
													"startlinecolor": "#2a3f5f"
												},
												"baxis": {
													"endlinecolor": "#2a3f5f",
													"gridcolor": "white",
													"linecolor": "white",
													"minorgridcolor": "white",
													"startlinecolor": "#2a3f5f"
												},
												"type": "carpet"
											}
										],
										"table": [
											{
												"cells": {
													"fill": {
														"color": "#EBF0F8"
													},
													"line": {
														"color": "white"
													}
												},
												"header": {
													"fill": {
														"color": "#C8D4E3"
													},
													"line": {
														"color": "white"
													}
												},
												"type": "table"
											}
										],
										"barpolar": [
											{
												"marker": {
													"line": {
														"color": "#E5ECF6",
														"width": 0.5
													},
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "barpolar"
											}
										],
										"pie": [
											{
												"automargin": true,
												"type": "pie"
											}
										]
									},
									"layout": {
										"autotypenumbers": "strict",
										"colorway": [
											"#636efa",
											"#EF553B",
											"#00cc96",
											"#ab63fa",
											"#FFA15A",
											"#19d3f3",
											"#FF6692",
											"#B6E880",
											"#FF97FF",
											"#FECB52"
										],
										"font": {
											"color": "#2a3f5f"
										},
										"hovermode": "closest",
										"hoverlabel": {
											"align": "left"
										},
										"paper_bgcolor": "white",
										"plot_bgcolor": "#E5ECF6",
										"polar": {
											"bgcolor": "#E5ECF6",
											"angularaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"radialaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											}
										},
										"ternary": {
											"bgcolor": "#E5ECF6",
											"aaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"baxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"caxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											}
										},
										"coloraxis": {
											"colorbar": {
												"outlinewidth": 0,
												"ticks": ""
											}
										},
										"colorscale": {
											"sequential": [
												[
													0,
													"#0d0887"
												],
												[
													0.1111111111111111,
													"#46039f"
												],
												[
													0.2222222222222222,
													"#7201a8"
												],
												[
													0.3333333333333333,
													"#9c179e"
												],
												[
													0.4444444444444444,
													"#bd3786"
												],
												[
													0.5555555555555556,
													"#d8576b"
												],
												[
													0.6666666666666666,
													"#ed7953"
												],
												[
													0.7777777777777778,
													"#fb9f3a"
												],
												[
													0.8888888888888888,
													"#fdca26"
												],
												[
													1,
													"#f0f921"
												]
											],
											"sequentialminus": [
												[
													0,
													"#0d0887"
												],
												[
													0.1111111111111111,
													"#46039f"
												],
												[
													0.2222222222222222,
													"#7201a8"
												],
												[
													0.3333333333333333,
													"#9c179e"
												],
												[
													0.4444444444444444,
													"#bd3786"
												],
												[
													0.5555555555555556,
													"#d8576b"
												],
												[
													0.6666666666666666,
													"#ed7953"
												],
												[
													0.7777777777777778,
													"#fb9f3a"
												],
												[
													0.8888888888888888,
													"#fdca26"
												],
												[
													1,
													"#f0f921"
												]
											],
											"diverging": [
												[
													0,
													"#8e0152"
												],
												[
													0.1,
													"#c51b7d"
												],
												[
													0.2,
													"#de77ae"
												],
												[
													0.3,
													"#f1b6da"
												],
												[
													0.4,
													"#fde0ef"
												],
												[
													0.5,
													"#f7f7f7"
												],
												[
													0.6,
													"#e6f5d0"
												],
												[
													0.7,
													"#b8e186"
												],
												[
													0.8,
													"#7fbc41"
												],
												[
													0.9,
													"#4d9221"
												],
												[
													1,
													"#276419"
												]
											]
										},
										"xaxis": {
											"gridcolor": "white",
											"linecolor": "white",
											"ticks": "",
											"title": {
												"standoff": 15
											},
											"zerolinecolor": "white",
											"automargin": true,
											"zerolinewidth": 2
										},
										"yaxis": {
											"gridcolor": "white",
											"linecolor": "white",
											"ticks": "",
											"title": {
												"standoff": 15
											},
											"zerolinecolor": "white",
											"automargin": true,
											"zerolinewidth": 2
										},
										"scene": {
											"xaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											},
											"yaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											},
											"zaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											}
										},
										"shapedefaults": {
											"line": {
												"color": "#2a3f5f"
											}
										},
										"annotationdefaults": {
											"arrowcolor": "#2a3f5f",
											"arrowhead": 0,
											"arrowwidth": 1
										},
										"geo": {
											"bgcolor": "white",
											"landcolor": "#E5ECF6",
											"subunitcolor": "white",
											"showland": true,
											"showlakes": true,
											"lakecolor": "white"
										},
										"title": {
											"x": 0.05
										},
										"mapbox": {
											"style": "light"
										}
									}
								},
								"xaxis": {
									"anchor": "y",
									"domain": [
										0,
										1
									],
									"title": {
										"text": "Data"
									}
								},
								"yaxis": {
									"anchor": "x",
									"domain": [
										0,
										1
									],
									"title": {
										"text": "value"
									}
								},
								"legend": {
									"title": {
										"text": "variable"
									},
									"tracegroupgap": 0
								},
								"title": {
									"text": "Hidratação e Atividade Física"
								},
								"barmode": "group"
							},
							"config": {
								"plotlyServerURL": "https://plot.ly"
							}
						},
						"text/html": "<div>                            <div id=\"a9da150d-e1da-4f92-a0d0-44b81673fd3b\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"a9da150d-e1da-4f92-a0d0-44b81673fd3b\")) {                    Plotly.newPlot(                        \"a9da150d-e1da-4f92-a0d0-44b81673fd3b\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"variable=Água\\u003cbr\\u003eData=%{x}\\u003cbr\\u003evalue=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Água\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Água\",\"offsetgroup\":\"Água\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"2025-10-01T00:00:00\",\"2025-10-02T00:00:00\",\"2025-10-03T00:00:00\",\"2025-10-04T00:00:00\",\"2025-10-05T00:00:00\",\"2025-10-06T00:00:00\",\"2025-10-07T00:00:00\",\"2025-10-08T00:00:00\",\"2025-10-09T00:00:00\",\"2025-10-10T00:00:00\"],\"xaxis\":\"x\",\"y\":[\"Não\",\"Não\",\"Sim\",\"Sim\",\"Não\",\"Não\",\"Não\",\"Sim\",\"Não\",\"Sim\"],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"hovertemplate\":\"variable=Atividade Física\\u003cbr\\u003eData=%{x}\\u003cbr\\u003evalue=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Atividade Física\",\"marker\":{\"color\":\"#EF553B\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Atividade Física\",\"offsetgroup\":\"Atividade Física\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"2025-10-01T00:00:00\",\"2025-10-02T00:00:00\",\"2025-10-03T00:00:00\",\"2025-10-04T00:00:00\",\"2025-10-05T00:00:00\",\"2025-10-06T00:00:00\",\"2025-10-07T00:00:00\",\"2025-10-08T00:00:00\",\"2025-10-09T00:00:00\",\"2025-10-10T00:00:00\"],\"xaxis\":\"x\",\"y\":[\"Sim\",\"Sim\",\"Sim\",\"Sim\",\"Não\",\"Não\",\"Não\",\"Não\",\"Não\",\"Sim\"],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Data\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"value\"}},\"legend\":{\"title\":{\"text\":\"variable\"},\"tracegroupgap\":0},\"title\":{\"text\":\"Hidratação e Atividade Física\"},\"barmode\":\"group\"},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('a9da150d-e1da-4f92-a0d0-44b81673fd3b');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
					},
					"metadata": {}
				},
				{
					"output_type": "execute_result",
					"execution_count": 6,
					"data": {
						"application/vnd.plotly.v1+json": {
							"data": [
								{
									"hovertemplate": "color=Normal<br>symbol=Normal<br>Data=%{x}<br>Glicemia (mg/dL)=%{y}<extra></extra>",
									"legendgroup": "Normal, Normal",
									"marker": {
										"color": "#636efa",
										"symbol": "circle"
									},
									"mode": "markers",
									"name": "Normal, Normal",
									"orientation": "v",
									"showlegend": true,
									"x": [
										"2025-10-01T00:00:00",
										"2025-10-02T00:00:00",
										"2025-10-03T00:00:00",
										"2025-10-04T00:00:00",
										"2025-10-05T00:00:00",
										"2025-10-06T00:00:00",
										"2025-10-07T00:00:00",
										"2025-10-09T00:00:00",
										"2025-10-10T00:00:00"
									],
									"xaxis": "x",
									"y": [
										162,
										152,
										74,
										166,
										131,
										80,
										162,
										134,
										147
									],
									"yaxis": "y",
									"type": "scatter"
								},
								{
									"hovertemplate": "color=Normal<br>symbol=Hiper<br>Data=%{x}<br>Glicemia (mg/dL)=%{y}<extra></extra>",
									"legendgroup": "Normal, Hiper",
									"marker": {
										"color": "#636efa",
										"symbol": "diamond"
									},
									"mode": "markers",
									"name": "Normal, Hiper",
									"orientation": "v",
									"showlegend": true,
									"x": [
										"2025-10-08T00:00:00"
									],
									"xaxis": "x",
									"y": [
										181
									],
									"yaxis": "y",
									"type": "scatter"
								}
							],
							"layout": {
								"template": {
									"data": {
										"histogram2dcontour": [
											{
												"type": "histogram2dcontour",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"choropleth": [
											{
												"type": "choropleth",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"histogram2d": [
											{
												"type": "histogram2d",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"heatmap": [
											{
												"type": "heatmap",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"heatmapgl": [
											{
												"type": "heatmapgl",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"contourcarpet": [
											{
												"type": "contourcarpet",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"contour": [
											{
												"type": "contour",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"surface": [
											{
												"type": "surface",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"mesh3d": [
											{
												"type": "mesh3d",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"scatter": [
											{
												"fillpattern": {
													"fillmode": "overlay",
													"size": 10,
													"solidity": 0.2
												},
												"type": "scatter"
											}
										],
										"parcoords": [
											{
												"type": "parcoords",
												"line": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterpolargl": [
											{
												"type": "scatterpolargl",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"bar": [
											{
												"error_x": {
													"color": "#2a3f5f"
												},
												"error_y": {
													"color": "#2a3f5f"
												},
												"marker": {
													"line": {
														"color": "#E5ECF6",
														"width": 0.5
													},
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "bar"
											}
										],
										"scattergeo": [
											{
												"type": "scattergeo",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterpolar": [
											{
												"type": "scatterpolar",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"histogram": [
											{
												"marker": {
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "histogram"
											}
										],
										"scattergl": [
											{
												"type": "scattergl",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatter3d": [
											{
												"type": "scatter3d",
												"line": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												},
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scattermapbox": [
											{
												"type": "scattermapbox",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterternary": [
											{
												"type": "scatterternary",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scattercarpet": [
											{
												"type": "scattercarpet",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"carpet": [
											{
												"aaxis": {
													"endlinecolor": "#2a3f5f",
													"gridcolor": "white",
													"linecolor": "white",
													"minorgridcolor": "white",
													"startlinecolor": "#2a3f5f"
												},
												"baxis": {
													"endlinecolor": "#2a3f5f",
													"gridcolor": "white",
													"linecolor": "white",
													"minorgridcolor": "white",
													"startlinecolor": "#2a3f5f"
												},
												"type": "carpet"
											}
										],
										"table": [
											{
												"cells": {
													"fill": {
														"color": "#EBF0F8"
													},
													"line": {
														"color": "white"
													}
												},
												"header": {
													"fill": {
														"color": "#C8D4E3"
													},
													"line": {
														"color": "white"
													}
												},
												"type": "table"
											}
										],
										"barpolar": [
											{
												"marker": {
													"line": {
														"color": "#E5ECF6",
														"width": 0.5
													},
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "barpolar"
											}
										],
										"pie": [
											{
												"automargin": true,
												"type": "pie"
											}
										]
									},
									"layout": {
										"autotypenumbers": "strict",
										"colorway": [
											"#636efa",
											"#EF553B",
											"#00cc96",
											"#ab63fa",
											"#FFA15A",
											"#19d3f3",
											"#FF6692",
											"#B6E880",
											"#FF97FF",
											"#FECB52"
										],
										"font": {
											"color": "#2a3f5f"
										},
										"hovermode": "closest",
										"hoverlabel": {
											"align": "left"
										},
										"paper_bgcolor": "white",
										"plot_bgcolor": "#E5ECF6",
										"polar": {
											"bgcolor": "#E5ECF6",
											"angularaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"radialaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											}
										},
										"ternary": {
											"bgcolor": "#E5ECF6",
											"aaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"baxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"caxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											}
										},
										"coloraxis": {
											"colorbar": {
												"outlinewidth": 0,
												"ticks": ""
											}
										},
										"colorscale": {
											"sequential": [
												[
													0,
													"#0d0887"
												],
												[
													0.1111111111111111,
													"#46039f"
												],
												[
													0.2222222222222222,
													"#7201a8"
												],
												[
													0.3333333333333333,
													"#9c179e"
												],
												[
													0.4444444444444444,
													"#bd3786"
												],
												[
													0.5555555555555556,
													"#d8576b"
												],
												[
													0.6666666666666666,
													"#ed7953"
												],
												[
													0.7777777777777778,
													"#fb9f3a"
												],
												[
													0.8888888888888888,
													"#fdca26"
												],
												[
													1,
													"#f0f921"
												]
											],
											"sequentialminus": [
												[
													0,
													"#0d0887"
												],
												[
													0.1111111111111111,
													"#46039f"
												],
												[
													0.2222222222222222,
													"#7201a8"
												],
												[
													0.3333333333333333,
													"#9c179e"
												],
												[
													0.4444444444444444,
													"#bd3786"
												],
												[
													0.5555555555555556,
													"#d8576b"
												],
												[
													0.6666666666666666,
													"#ed7953"
												],
												[
													0.7777777777777778,
													"#fb9f3a"
												],
												[
													0.8888888888888888,
													"#fdca26"
												],
												[
													1,
													"#f0f921"
												]
											],
											"diverging": [
												[
													0,
													"#8e0152"
												],
												[
													0.1,
													"#c51b7d"
												],
												[
													0.2,
													"#de77ae"
												],
												[
													0.3,
													"#f1b6da"
												],
												[
													0.4,
													"#fde0ef"
												],
												[
													0.5,
													"#f7f7f7"
												],
												[
													0.6,
													"#e6f5d0"
												],
												[
													0.7,
													"#b8e186"
												],
												[
													0.8,
													"#7fbc41"
												],
												[
													0.9,
													"#4d9221"
												],
												[
													1,
													"#276419"
												]
											]
										},
										"xaxis": {
											"gridcolor": "white",
											"linecolor": "white",
											"ticks": "",
											"title": {
												"standoff": 15
											},
											"zerolinecolor": "white",
											"automargin": true,
											"zerolinewidth": 2
										},
										"yaxis": {
											"gridcolor": "white",
											"linecolor": "white",
											"ticks": "",
											"title": {
												"standoff": 15
											},
											"zerolinecolor": "white",
											"automargin": true,
											"zerolinewidth": 2
										},
										"scene": {
											"xaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											},
											"yaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											},
											"zaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											}
										},
										"shapedefaults": {
											"line": {
												"color": "#2a3f5f"
											}
										},
										"annotationdefaults": {
											"arrowcolor": "#2a3f5f",
											"arrowhead": 0,
											"arrowwidth": 1
										},
										"geo": {
											"bgcolor": "white",
											"landcolor": "#E5ECF6",
											"subunitcolor": "white",
											"showland": true,
											"showlakes": true,
											"lakecolor": "white"
										},
										"title": {
											"x": 0.05
										},
										"mapbox": {
											"style": "light"
										}
									}
								},
								"xaxis": {
									"anchor": "y",
									"domain": [
										0,
										1
									],
									"title": {
										"text": "Data"
									}
								},
								"yaxis": {
									"anchor": "x",
									"domain": [
										0,
										1
									],
									"title": {
										"text": "Glicemia (mg/dL)"
									}
								},
								"legend": {
									"title": {
										"text": "color, symbol"
									},
									"tracegroupgap": 0
								},
								"title": {
									"text": "Risco de Hipo/Hiperglicemia"
								}
							},
							"config": {
								"plotlyServerURL": "https://plot.ly"
							}
						},
						"text/html": "<div>                            <div id=\"81b795e7-fb2b-4dc6-8e7d-53dd6e2285b8\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"81b795e7-fb2b-4dc6-8e7d-53dd6e2285b8\")) {                    Plotly.newPlot(                        \"81b795e7-fb2b-4dc6-8e7d-53dd6e2285b8\",                        [{\"hovertemplate\":\"color=Normal\\u003cbr\\u003esymbol=Normal\\u003cbr\\u003eData=%{x}\\u003cbr\\u003eGlicemia (mg\\u002fdL)=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Normal, Normal\",\"marker\":{\"color\":\"#636efa\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Normal, Normal\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2025-10-01T00:00:00\",\"2025-10-02T00:00:00\",\"2025-10-03T00:00:00\",\"2025-10-04T00:00:00\",\"2025-10-05T00:00:00\",\"2025-10-06T00:00:00\",\"2025-10-07T00:00:00\",\"2025-10-09T00:00:00\",\"2025-10-10T00:00:00\"],\"xaxis\":\"x\",\"y\":[162,152,74,166,131,80,162,134,147],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"color=Normal\\u003cbr\\u003esymbol=Hiper\\u003cbr\\u003eData=%{x}\\u003cbr\\u003eGlicemia (mg\\u002fdL)=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Normal, Hiper\",\"marker\":{\"color\":\"#636efa\",\"symbol\":\"diamond\"},\"mode\":\"markers\",\"name\":\"Normal, Hiper\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2025-10-08T00:00:00\"],\"xaxis\":\"x\",\"y\":[181],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Data\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Glicemia (mg\\u002fdL)\"}},\"legend\":{\"title\":{\"text\":\"color, symbol\"},\"tracegroupgap\":0},\"title\":{\"text\":\"Risco de Hipo\\u002fHiperglicemia\"}},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('81b795e7-fb2b-4dc6-8e7d-53dd6e2285b8');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
					},
					"metadata": {}
				},
				{
					"output_type": "execute_result",
					"execution_count": 6,
					"data": {
						"application/vnd.plotly.v1+json": {
							"data": [
								{
									"alignmentgroup": "True",
									"hovertemplate": "Data=%{x}<br>Adesão (%)=%{y}<extra></extra>",
									"legendgroup": "",
									"marker": {
										"color": "#636efa",
										"pattern": {
											"shape": ""
										}
									},
									"name": "",
									"offsetgroup": "",
									"orientation": "v",
									"showlegend": false,
									"textposition": "auto",
									"x": [
										"2025-10-01T00:00:00",
										"2025-10-02T00:00:00",
										"2025-10-03T00:00:00",
										"2025-10-04T00:00:00",
										"2025-10-05T00:00:00",
										"2025-10-06T00:00:00",
										"2025-10-07T00:00:00",
										"2025-10-08T00:00:00",
										"2025-10-09T00:00:00",
										"2025-10-10T00:00:00"
									],
									"xaxis": "x",
									"y": [
										0,
										0,
										100,
										0,
										100,
										0,
										100,
										0,
										0,
										100
									],
									"yaxis": "y",
									"type": "bar"
								}
							],
							"layout": {
								"template": {
									"data": {
										"histogram2dcontour": [
											{
												"type": "histogram2dcontour",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"choropleth": [
											{
												"type": "choropleth",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"histogram2d": [
											{
												"type": "histogram2d",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"heatmap": [
											{
												"type": "heatmap",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"heatmapgl": [
											{
												"type": "heatmapgl",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"contourcarpet": [
											{
												"type": "contourcarpet",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"contour": [
											{
												"type": "contour",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"surface": [
											{
												"type": "surface",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												},
												"colorscale": [
													[
														0,
														"#0d0887"
													],
													[
														0.1111111111111111,
														"#46039f"
													],
													[
														0.2222222222222222,
														"#7201a8"
													],
													[
														0.3333333333333333,
														"#9c179e"
													],
													[
														0.4444444444444444,
														"#bd3786"
													],
													[
														0.5555555555555556,
														"#d8576b"
													],
													[
														0.6666666666666666,
														"#ed7953"
													],
													[
														0.7777777777777778,
														"#fb9f3a"
													],
													[
														0.8888888888888888,
														"#fdca26"
													],
													[
														1,
														"#f0f921"
													]
												]
											}
										],
										"mesh3d": [
											{
												"type": "mesh3d",
												"colorbar": {
													"outlinewidth": 0,
													"ticks": ""
												}
											}
										],
										"scatter": [
											{
												"fillpattern": {
													"fillmode": "overlay",
													"size": 10,
													"solidity": 0.2
												},
												"type": "scatter"
											}
										],
										"parcoords": [
											{
												"type": "parcoords",
												"line": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterpolargl": [
											{
												"type": "scatterpolargl",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"bar": [
											{
												"error_x": {
													"color": "#2a3f5f"
												},
												"error_y": {
													"color": "#2a3f5f"
												},
												"marker": {
													"line": {
														"color": "#E5ECF6",
														"width": 0.5
													},
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "bar"
											}
										],
										"scattergeo": [
											{
												"type": "scattergeo",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterpolar": [
											{
												"type": "scatterpolar",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"histogram": [
											{
												"marker": {
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "histogram"
											}
										],
										"scattergl": [
											{
												"type": "scattergl",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatter3d": [
											{
												"type": "scatter3d",
												"line": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												},
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scattermapbox": [
											{
												"type": "scattermapbox",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scatterternary": [
											{
												"type": "scatterternary",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"scattercarpet": [
											{
												"type": "scattercarpet",
												"marker": {
													"colorbar": {
														"outlinewidth": 0,
														"ticks": ""
													}
												}
											}
										],
										"carpet": [
											{
												"aaxis": {
													"endlinecolor": "#2a3f5f",
													"gridcolor": "white",
													"linecolor": "white",
													"minorgridcolor": "white",
													"startlinecolor": "#2a3f5f"
												},
												"baxis": {
													"endlinecolor": "#2a3f5f",
													"gridcolor": "white",
													"linecolor": "white",
													"minorgridcolor": "white",
													"startlinecolor": "#2a3f5f"
												},
												"type": "carpet"
											}
										],
										"table": [
											{
												"cells": {
													"fill": {
														"color": "#EBF0F8"
													},
													"line": {
														"color": "white"
													}
												},
												"header": {
													"fill": {
														"color": "#C8D4E3"
													},
													"line": {
														"color": "white"
													}
												},
												"type": "table"
											}
										],
										"barpolar": [
											{
												"marker": {
													"line": {
														"color": "#E5ECF6",
														"width": 0.5
													},
													"pattern": {
														"fillmode": "overlay",
														"size": 10,
														"solidity": 0.2
													}
												},
												"type": "barpolar"
											}
										],
										"pie": [
											{
												"automargin": true,
												"type": "pie"
											}
										]
									},
									"layout": {
										"autotypenumbers": "strict",
										"colorway": [
											"#636efa",
											"#EF553B",
											"#00cc96",
											"#ab63fa",
											"#FFA15A",
											"#19d3f3",
											"#FF6692",
											"#B6E880",
											"#FF97FF",
											"#FECB52"
										],
										"font": {
											"color": "#2a3f5f"
										},
										"hovermode": "closest",
										"hoverlabel": {
											"align": "left"
										},
										"paper_bgcolor": "white",
										"plot_bgcolor": "#E5ECF6",
										"polar": {
											"bgcolor": "#E5ECF6",
											"angularaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"radialaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											}
										},
										"ternary": {
											"bgcolor": "#E5ECF6",
											"aaxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"baxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											},
											"caxis": {
												"gridcolor": "white",
												"linecolor": "white",
												"ticks": ""
											}
										},
										"coloraxis": {
											"colorbar": {
												"outlinewidth": 0,
												"ticks": ""
											}
										},
										"colorscale": {
											"sequential": [
												[
													0,
													"#0d0887"
												],
												[
													0.1111111111111111,
													"#46039f"
												],
												[
													0.2222222222222222,
													"#7201a8"
												],
												[
													0.3333333333333333,
													"#9c179e"
												],
												[
													0.4444444444444444,
													"#bd3786"
												],
												[
													0.5555555555555556,
													"#d8576b"
												],
												[
													0.6666666666666666,
													"#ed7953"
												],
												[
													0.7777777777777778,
													"#fb9f3a"
												],
												[
													0.8888888888888888,
													"#fdca26"
												],
												[
													1,
													"#f0f921"
												]
											],
											"sequentialminus": [
												[
													0,
													"#0d0887"
												],
												[
													0.1111111111111111,
													"#46039f"
												],
												[
													0.2222222222222222,
													"#7201a8"
												],
												[
													0.3333333333333333,
													"#9c179e"
												],
												[
													0.4444444444444444,
													"#bd3786"
												],
												[
													0.5555555555555556,
													"#d8576b"
												],
												[
													0.6666666666666666,
													"#ed7953"
												],
												[
													0.7777777777777778,
													"#fb9f3a"
												],
												[
													0.8888888888888888,
													"#fdca26"
												],
												[
													1,
													"#f0f921"
												]
											],
											"diverging": [
												[
													0,
													"#8e0152"
												],
												[
													0.1,
													"#c51b7d"
												],
												[
													0.2,
													"#de77ae"
												],
												[
													0.3,
													"#f1b6da"
												],
												[
													0.4,
													"#fde0ef"
												],
												[
													0.5,
													"#f7f7f7"
												],
												[
													0.6,
													"#e6f5d0"
												],
												[
													0.7,
													"#b8e186"
												],
												[
													0.8,
													"#7fbc41"
												],
												[
													0.9,
													"#4d9221"
												],
												[
													1,
													"#276419"
												]
											]
										},
										"xaxis": {
											"gridcolor": "white",
											"linecolor": "white",
											"ticks": "",
											"title": {
												"standoff": 15
											},
											"zerolinecolor": "white",
											"automargin": true,
											"zerolinewidth": 2
										},
										"yaxis": {
											"gridcolor": "white",
											"linecolor": "white",
											"ticks": "",
											"title": {
												"standoff": 15
											},
											"zerolinecolor": "white",
											"automargin": true,
											"zerolinewidth": 2
										},
										"scene": {
											"xaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											},
											"yaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											},
											"zaxis": {
												"backgroundcolor": "#E5ECF6",
												"gridcolor": "white",
												"linecolor": "white",
												"showbackground": true,
												"ticks": "",
												"zerolinecolor": "white",
												"gridwidth": 2
											}
										},
										"shapedefaults": {
											"line": {
												"color": "#2a3f5f"
											}
										},
										"annotationdefaults": {
											"arrowcolor": "#2a3f5f",
											"arrowhead": 0,
											"arrowwidth": 1
										},
										"geo": {
											"bgcolor": "white",
											"landcolor": "#E5ECF6",
											"subunitcolor": "white",
											"showland": true,
											"showlakes": true,
											"lakecolor": "white"
										},
										"title": {
											"x": 0.05
										},
										"mapbox": {
											"style": "light"
										}
									}
								},
								"xaxis": {
									"anchor": "y",
									"domain": [
										0,
										1
									],
									"title": {
										"text": "Data"
									}
								},
								"yaxis": {
									"anchor": "x",
									"domain": [
										0,
										1
									],
									"title": {
										"text": "Adesão (%)"
									}
								},
								"legend": {
									"tracegroupgap": 0
								},
								"title": {
									"text": "Adesão à Medicação"
								},
								"barmode": "relative"
							},
							"config": {
								"plotlyServerURL": "https://plot.ly"
							}
						},
						"text/html": "<div>                            <div id=\"0749d6a7-40c1-4fea-82ff-8b00be3bc1ba\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"0749d6a7-40c1-4fea-82ff-8b00be3bc1ba\")) {                    Plotly.newPlot(                        \"0749d6a7-40c1-4fea-82ff-8b00be3bc1ba\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"Data=%{x}\\u003cbr\\u003eAdesão (%)=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"2025-10-01T00:00:00\",\"2025-10-02T00:00:00\",\"2025-10-03T00:00:00\",\"2025-10-04T00:00:00\",\"2025-10-05T00:00:00\",\"2025-10-06T00:00:00\",\"2025-10-07T00:00:00\",\"2025-10-08T00:00:00\",\"2025-10-09T00:00:00\",\"2025-10-10T00:00:00\"],\"xaxis\":\"x\",\"y\":[0,0,100,0,100,0,100,0,0,100],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Data\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Adesão (%)\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Adesão à Medicação\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('0749d6a7-40c1-4fea-82ff-8b00be3bc1ba');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
					},
					"metadata": {}
				}
			],
			"execution_count": 6
		},
		{
			"id": "68fb8d1b18f38dc849cfa7a0",
			"cell_type": "code",
			"source": "",
			"metadata": {
				"collapsed": false,
				"scrolled": false,
				"datarobot": {
					"language": "python"
				},
				"hide_code": false,
				"hide_results": false,
				"disable_run": false,
				"chart_settings": null,
				"custom_metric_settings": null,
				"custom_llm_metric_settings": null,
				"dataframe_view_options": null
			},
			"outputs": [],
			"execution_count": null
		}
	],
	"metadata": {
		"kernelspec": {
			"name": "python",
			"language": "python",
			"display_name": "Python 3.11"
		},
		"language_info": {
			"name": "python",
			"version": "3.11"
		}
	},
	"nbformat": 4,
	"nbformat_minor": 5
}