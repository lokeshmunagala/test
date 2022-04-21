from django.shortcuts import render
import pandas as pd


def index(request):
    """view function for sales app"""

    # read data

    # 2021 Data

    bronx2020 = pd.read_csv("sales/data/2020_bronx.csv")
    bronx2021 = pd.read_csv("sales/data/2021_bronx.csv")
    bronx2020.columns = [
        "BOROUGH",
        "NEIGHBORHOOD",
        "BUILDING CLASS CATEGORY",
        "TAX CLASS AT PRESENT",
        "BLOCK",
        "LOT",
        "EASE-MENT",
        "BUILDING CLASS AT PRESENT",
        "ADDRESS",
        "APARTMENT NUMBER",
        "ZIP CODE",
        "RESIDENTIAL UNITS",
        "COMMERCIAL UNITS",
        "TOTAL UNITS",
        "LAND SQUARE FEET",
        "GROSS SQUARE FEET",
        "YEAR BUILT",
        "TAX CLASS AT TIME OF SALE",
        "BUILDING CLASS AT TIME OF SALE",
        "SALE PRICE",
        "SALE DATE",
    ]

    bronx2021.columns = bronx2020.columns

    bronx2021 = bronx2021.drop(
        [
            "BOROUGH",
            "BUILDING CLASS CATEGORY",
            "TAX CLASS AT PRESENT",
            "BLOCK",
            "LOT",
            "EASE-MENT",
            "BUILDING CLASS AT PRESENT",
            "ADDRESS",
            "APARTMENT NUMBER",
            "ZIP CODE",
            "RESIDENTIAL UNITS",
            "COMMERCIAL UNITS",
            "TOTAL UNITS",
            "LAND SQUARE FEET",
            "GROSS SQUARE FEET",
            "YEAR BUILT",
            "TAX CLASS AT TIME OF SALE",
            "BUILDING CLASS AT TIME OF SALE",
            "SALE DATE",
        ],
        axis=1,
    )
    bronx2021["SALE PRICE"] = bronx2021["SALE PRICE"].astype(str)
    bronx2021["SALE PRICE"] = bronx2021["SALE PRICE"].apply(
        lambda x: x.replace(",", "")
    )
    bronx2021["SALE PRICE"] = bronx2021["SALE PRICE"].replace(" ", "0")
    bronx2021["SALE PRICE"] = bronx2021["SALE PRICE"].replace(" -   ", "0")
    bronx2021["SALE PRICE"] = pd.to_numeric(bronx2020["SALE PRICE"], errors="coerce")
    bronx2021.dropna(inplace=True)
    bronx2021["SALE PRICE"] = bronx2021["SALE PRICE"].astype(float) * 10
    df2021 = bronx2021.groupby(["NEIGHBORHOOD"]).sum().reset_index()

    categories = list(df2021["NEIGHBORHOOD"])
    values = list(df2021["SALE PRICE"])

    table_content = df2021.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace(
        'class="dataframe"', "class='table table-striped'"
    )
    table_content = table_content.replace('border="1"', "")

    context = {"categories": categories, "values": values, "table_data": table_content}
    return render(request, "index.html", context=context)

    # 2021 Data ends -----------------------------------------------------------------------------------

    # 2020 Data starts -----------------------------------------------------------------------------------

    bronx2020 = pd.read_csv("sales/data/2020_bronx.csv")
    bronx2021 = pd.read_csv("sales/data/2021_bronx.csv")
    bronx2020.columns = [
        "BOROUGH",
        "NEIGHBORHOOD",
        "BUILDING CLASS CATEGORY",
        "TAX CLASS AT PRESENT",
        "BLOCK",
        "LOT",
        "EASE-MENT",
        "BUILDING CLASS AT PRESENT",
        "ADDRESS",
        "APARTMENT NUMBER",
        "ZIP CODE",
        "RESIDENTIAL UNITS",
        "COMMERCIAL UNITS",
        "TOTAL UNITS",
        "LAND SQUARE FEET",
        "GROSS SQUARE FEET",
        "YEAR BUILT",
        "TAX CLASS AT TIME OF SALE",
        "BUILDING CLASS AT TIME OF SALE",
        "SALE PRICE",
        "SALE DATE",
    ]

    bronx2020["SALE PRICE"] = bronx2020["SALE PRICE"].astype(str)
    bronx2020["SALE PRICE"] = bronx2020["SALE PRICE"].apply(
        lambda x: x.replace(",", "")
    )
    bronx2020["SALE PRICE"] = bronx2020["SALE PRICE"].replace(" ", "0")
    bronx2020["SALE PRICE"] = bronx2020["SALE PRICE"].replace(" -   ", "0")
    bronx2020["SALE PRICE"] = pd.to_numeric(bronx2020["SALE PRICE"], errors="coerce")
    bronx2020.dropna(inplace=True)
    bronx2020["SALE PRICE"] = bronx2020["SALE PRICE"].astype(float) * 10
    df2020 = bronx2020.groupby(["NEIGHBORHOOD"]).sum().reset_index()

    cat = list(df2020["NEIGHBORHOOD"])
    val = list(df2020["SALE PRICE"])

    table_content1 = df2020.to_html(index=None)
    table_content1 = table_content1.replace("", "")
    table_content1 = table_content1.replace(
        'class="dataframe"', "class='table table-striped'"
    )
    table_content1 = table_content1.replace('border="1"', "")

    context1 = {"cat": cat, "val": val, "table_data": table_content1}
    return render(request, "index.html", context=context1)


# 2020 Data ends -----------------------------------------------------------------------------------
