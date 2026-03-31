import pandas as pd
from pathlib import Path

out = []
base_path = Path('e:/repo/PriceAction_Fisica/WESQUAD/DadosCandlesBacktest')
folders = ['2012_14','2014_16','2016_18','2018_20','2020_22','2022_24','2024_26']
all_data = {}

for folder in folders:
    folder_path = base_path / folder
    csv_files = sorted(folder_path.glob('*.csv'))
    out.append(f'{folder}: {len(csv_files)} csv files')
    dfs = []
    for csv_file in csv_files:
        read_success = False
        for enc in ['latin1', 'utf-8', 'cp1252']:
            try:
                df = pd.read_csv(csv_file, sep=';', decimal=',', encoding=enc)
                df['ArquivoOrigem'] = csv_file.stem
                dfs.append(df)
                read_success = True
                out.append(f'{folder} {csv_file.name}: read ok {enc}, rows {len(df)}')
                break
            except Exception as e:
                out.append(f'{folder} {csv_file.name}: failed {enc} -> {e}')
        if not read_success:
            out.append(f'{folder} {csv_file.name}: failed all encodings')
    if dfs:
        all_data[folder] = pd.concat(dfs, ignore_index=True)
        out.append(f'{folder}: loaded {len(all_data[folder])} rows')

all_clean = {}
for folder, df in all_data.items():
    dfc = df.copy()
    dfc.columns = dfc.columns.str.strip()
    if 'Data' in dfc.columns:
        dfc['Data'] = pd.to_datetime(dfc['Data'], format='%d/%m/%Y', errors='coerce')
    if 'Hora' in dfc.columns:
        dfc['Hora'] = pd.to_datetime(dfc['Hora'], format='%H:%M:%S', errors='coerce').dt.time
    for col in ['Abertura','Máximo','Mínimo','Fechamento','Volume','Quantidade']:
        if col in dfc.columns:
            dfc[col] = pd.to_numeric(dfc[col].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False), errors='coerce')
    dfc = dfc.dropna(subset=['Data','Fechamento'], how='any')
    all_clean[folder] = dfc
    out.append(f'{folder}: cleaned {len(dfc)} rows')

if all_clean:
    consolidated = pd.concat(all_clean.values(), ignore_index=True)
    out.append(f'consolidated rows {len(consolidated)}')

    if 'Ativo' in consolidated.columns:
        metricas = {}
        for ativo, group in consolidated.groupby('Ativo'):
            group2 = group.sort_values('Data')
            if len(group2) < 2:
                continue
            taxa = (group2['Fechamento'] > group2['Abertura']).mean() * 100
            amp = (group2['Máximo'] - group2['Mínimo']).mean()
            metricas[ativo] = {'taxa_ganho': taxa, 'amplitude': amp, 'candles': len(group2)}

        top = sorted(metricas.items(), key=lambda x: x[1]['taxa_ganho'], reverse=True)
        out.append('top 5 ativos por taxa de ganho:')
        for ativo, m in top[:5]:
            out.append(f'{ativo}: {m}')

        top_vol = sorted(metricas.items(), key=lambda x: x[1]['amplitude'], reverse=True)
        out.append('top 5 ativos por amplitude:')
        for ativo, m in top_vol[:5]:
            out.append(f'{ativo}: {m}')

with open('e:/repo/PriceAction_Fisica/WESQUAD/temp_analysis_out.txt','w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print('Done writing output to temp_analysis_out.txt')
