T=("http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/2008/media_alunos_turma_municipios_2008.zip" \
"http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/2009/media_alunos_turma_municipios_2009.zip" \
"http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/2010/media_alunos_turma_municipios_2010_3.zip")

for i in ${T[*]}; do \
    curl -O $i; \
    unzip -o *.zip; \
    rm *.zip;done

mv *.xls ./data

