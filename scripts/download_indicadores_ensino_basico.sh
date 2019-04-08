T=("http://api.pgi.gov.br/api/1/serie/2555.json" \
"http://api.pgi.gov.br/api/1/serie/2620.json" \
"http://api.pgi.gov.br/api/1/serie/1703.json")

for i in ${T[*]}; do \
    curl -O $i;done

mv *.json ./data

