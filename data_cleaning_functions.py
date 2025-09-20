def clean_outliers(column, fquantile=0.25, lquantile=0.75):
    Q1 = column.quantile(fquantile)
    Q3 = column.quantile(lquantile)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    mean_val = column.mean()
    column = column.where((column >= lower) & (column <= upper), mean_val)

    return column

