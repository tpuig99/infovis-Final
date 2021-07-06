#!/bin/sh

echo "Downloading and unzipping dataset from https://sisa.msal.gov.ar/datos/descargas/covid-19/files/datos_nomivac_covid19.zip "
curl -sS https://sisa.msal.gov.ar/datos/descargas/covid-19/files/datos_nomivac_covid19.zip > datos_nomivac_covid19.zip && \
unzip datos_nomivac_covid19.zip                                  && \
rm datos_nomivac_covid19.zip

export PGPASSWORD=$4

echo "Dropping \"vacunas\" table (if it exists)"
psql -h $1 -d $2 -U $3 -c "DROP table if exists vacunas"

echo "Creating table \"vacunas\""
psql -h $1 -d $2 -U $3 -c "create table vacunas
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

echo "Populating \"vacunas\" table with downloded dataset"
psql -h $1 -d $2 -U $3 -c "\copy vacunas from 'datos_nomivac_covid19.csv' DELIMITER ',' CSV HEADER;"

echo "Altering \"vacunas\" for our APIs internal use"
psql -h $1 -d $2 -U $3 -c "ALTER TABLE vacunas ADD COLUMN id SERIAL PRIMARY KEY;"

echo "Deleting downloaded dataset file"
rm datos_nomivac_covid19.csv
