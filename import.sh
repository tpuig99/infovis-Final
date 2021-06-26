#!/bin/sh

curl -sS https://sisa.msal.gov.ar/datos/descargas/covid-19/files/datos_nomivac_covid19.zip > datos_nomivac_covid19.zip && \
unzip datos_nomivac_covid19.zip                                  && \
rm datos_nomivac_covid19.zip

export PGPASSWORD='password'
psql -h localhost -d infovis -U postgres -c "DROP table if exists vacunas"
psql -h localhost -d infovis -U postgres -c "create table vacunas
(
    sexo                       text,
    grupo_etario               text,
    jurisdiccion_residencia    text,
    jurisdiccion_residencia_id integer,
    depto_residencia           text,
    depto_residencia_id        integer,
    jurisdiccion_aplicacion    text,
    jurisdiccion_aplicacion_id integer,
    depto_aplicacion           text,
    depto_aplicacion_id        integer,
    fecha_aplicacion           text,
    vacuna                     text,
    condicion_aplicacion       text,
    orden_dosis                integer,
    lote_vacuna                text
);"

psql -h localhost -d infovis -U postgres -c "\copy vacunas from 'datos_nomivac_covid19.csv' DELIMITER ',' CSV HEADER;"
psql -h localhost -d infovis -U postgres -c "ALTER TABLE vacunas ADD COLUMN id SERIAL PRIMARY KEY;"

rm datos_nomivac_covid19.csv
