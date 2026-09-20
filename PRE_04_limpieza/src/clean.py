import os

import pandas as pd

INPUT_FILE = "PRE_04_limpieza/data/ventas.csv"
OUTPUT_FILE = "PRE_04_limpieza/submission/ventas.csv"

SUPPLIER_REPLACEMENTS = {
    "Bancolombia S.A.": [
        "BANCOLOMBIA S.A.",
    ],
    "Corona S.A.S.": [
        "Corona SAS",
    ],
    "Ecopetrol S.A.": [
        "Ecopetrol  S.A.",
    ],
    "Google Colombia Ltda.": [
        "GOOGLE COLOMBIA LTDA.",
    ],
    "Grupo Éxito S.A.": [
        "Grupo  Éxito  S.A.",
    ],
    "Microsoft Colombia Inc.": [
        "MICROSOFT COLOMBIA INC.",
	],
    "Postobon S.A.": [
        "POSTOBON S.A.",
        "POSTOBÓN S.A.",
    ],
    "SAP Colombia S.A.S.": [
    	"SAP Colombia SAS",
        "SAP Colombia S.A.S",
    ],
    "Sura S.A.": [
        "Sura  S.A",
        "Sura  S.A.",
    ],
    "Telefónica Colombia": [
        "Telefónica  Colombia",
    ],
    "Oracle Colombia Ltda.": [
        "oracle colombia ltda",
        "oracle colombia ltda.",
        "Oracle Colombia",
    ],
    "IBM Colombia S.A.S.": [
        "ibm colombia s.a.s.",
        "IBM Colombia SAS.",
    ],
    "Siemens S.A.S.": [
        "siemens s.a.s.",
        "SIEMENS S.A.S.",
    ],
    "Schneider Electric": [
        "Schneider  Electric",
    ],
    "Amazon Web Services Colombia": [
        "amazon web services colombia",
    ],
    "Cementos Argos S.A.": [
        "cementos argos s.a.",
        "Cementos Argos SA",
    ],
    "Nutresa S.A.": [
        "Nutresa SA",
        "nutresa s.a.",
    ],
}

COUNTRY_REPLACEMENTS = {
    "Colombia": [
        "CO",
        "COL",
        "colombia",
        "COLOMBIA",
    ]
}

CITY_REPLACEMENTS = {
    "Bogotá": [
        "BOGOTÁ",
        "Bogotá",
        "bogotá"
    ],
    "Medellín": [
        "MEDELLÍN",
        "Medellin",
        "medellín",
    ],
}   

def make_replacements(series, replacements):
    for replacement, values in replacements.items():
        for value in values:
            series = series.replace(value, replacement)
    return series

def strip_whitespace(series):
    return series.str.strip()

def to_lowercase(series):
    return series.str.lower()

def replace_space_with_underscore(series):
    return series.str.replace(" ", "_")

def clean_column_names(df):
    df.columns = strip_whitespace(df.columns)
    df.columns = to_lowercase(df.columns)
    df.columns = replace_space_with_underscore(df.columns)
    return df


def clean_supplier_column(series):
    series = strip_whitespace(series)
    series = make_replacements(series, SUPPLIER_REPLACEMENTS)
    return series

def clean_country_column(series):
    series = strip_whitespace(series)
    series = make_replacements(series, COUNTRY_REPLACEMENTS)
    return series

def clean_city_column(series):
    series = strip_whitespace(series)
    series = make_replacements(series, CITY_REPLACEMENTS)
    return series

def clean_purchase_date_column(series):
    series = strip_whitespace(series)
    series = series.str.replace(r".", "-", regex=False)
    return series

def main():

    df = pd.read_csv(INPUT_FILE)

    df = clean_column_names(df)
    
    df["supplier"] = clean_supplier_column(df["supplier"])
    df["country"] = clean_country_column(df["country"])
    df["city"] = clean_city_column(df["city"])
    df["purchase_date"] = clean_purchase_date_column(df["purchase_date"])
    
    df.to_csv(OUTPUT_FILE, index=False)

    

if __name__ == "_main_":
    main()