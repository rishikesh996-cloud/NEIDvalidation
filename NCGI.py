import pandas as pd

df_main = pd.read_excel("data.xlsx")

df_3500 = pd.read_excel("final.xlsx", sheet_name="3500")
df_700 = pd.read_excel("final.xlsx", sheet_name="700")

# 3500 sheet
df_3500_sel = df_3500[["SAP", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]].rename(
    columns={
        1: "B_3500",
        2: "C_3500", 3: "D_3500", 4: "E_3500",
        5: "F_3500", 6: "G_3500", 7: "H_3500",
        8: "I_3500", 9: "J_3500", 10: "K_3500",
        11: "L_3500", 12: "M_3500", 13: "N_3500"
    }
)

# 700 sheet
df_700_sel = df_700[["SAP", 16, 17, 18, 19, 20, 21]].rename(
    columns={
        16: "C_700", 17: "D_700", 18: "E_700",
        19: "F_700", 20: "G_700", 21: "H_700"
    }
)

# Merge
result = pd.merge(df_main, df_3500_sel, on="SAP", how="left")
result = pd.merge(result, df_700_sel, on="SAP", how="left")

# Save output
result.to_excel("output.xlsx", index=False)