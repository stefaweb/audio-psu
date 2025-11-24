#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Thermal comparison for MOSFETs used in the UC3845A DC-DC 24V → 450V flyback.

Version : 2.9.8
Authors: stef and ChatGPT

Date: 23-11-2025

Python dependencies:
    pip install numpy pandas matplotlib
    
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

# ==============================================================
# 1) CIRCUIT PARAMETERS
# ==============================================================

Vin      = 24      # Volts
Vout     = 450     # Volts
Iout     = 0.120   # Ampere

# Flyback frequency
fsw      = 50      # kHz

Np       = 10      # Number of Primary Turns
Ns       = 190     # Number of Secondary Turns
Lp       = 68      # µH
Llk      = 0.454   # µH
Vgs      = 10.0    # Volts
Ig_max   = 1       # Ampere - UC3845A Iout max
dvdt_max = 10      # V/ns

# Ambient temperature (Ta)
Tamb     = 25      # °C

# Heatsink parameters
Rth_model = "Fischer SK-437-50-STS"
Rth_CS    = 0.50
Rth_SA    = 14.0

# Temperature unit: "C" for Celsius, "K" for Kelvin
TEMP_UNIT = "C"   # changer en "K" pour travailler en Kelvin

# ==============================================================
# 2) AUTOMATIC PRIMARY CALCULATION
# ==============================================================

# Unit conversion
Lp_H     = Lp  * 1e-6       # µH → H
Llk_H    = Llk * 1e-6       # µH → H
fsw_Hz   = fsw * 1e3        # kHz → Hz
dvdt_max = dvdt_max * 1e9   # V/ns → V/s

Vref = Vout * (Np / Ns)
V_L_on = Vin - 0.8

# Temperature converter
def convert_temp(T):
    """Return temperature in the selected unit."""
    if TEMP_UNIT.upper() == "K":
        return T + 273.15
    return T

# Duty cycle (flyback discontinu theoretical equation)
D_theoretical = Vref / (Vin + Vref)

# UC3845A limitation: MAX duty = 50%
D = min(D_theoretical, 0.50)

Ipk = V_L_on * D / (Lp_H * fsw_Hz)
Irms = Ipk * np.sqrt(D / 3)

Vds_peak = Vin + Vref + Ipk * np.sqrt(Llk_H / Lp_H) * Vin * 0.45
if Vds_peak < Vin + Vref:
    Vds_peak = Vin + Vref + 5
Vds = Vds_peak

def compute_r1_simple(Qgd, tr, tf):
    Qgd_nC = Qgd * 1e9

    # Base recommendation from Qgd
    if Qgd_nC < 5:
        R1_nom = 8
        span = 2
    elif Qgd_nC < 10:
        R1_nom = 11
        span = 2
    else:
        R1_nom = 18
        span = 4

    # Adjust for switching speed
    tsw_ns = (tr + tf) * 1e9
    if tsw_ns < 20:
        R1_nom += 4
    elif tsw_ns > 60:
        R1_nom -= 2

    return max(R1_nom - span, 0), R1_nom + span
    

# ==============================================================
# 3) MOSFET DATA (UNITS AS IN DATASHEET)
# ==============================================================

mosfets = {

    "IRFB4615PBF": {
        "Vds": 150,
        "Rg": 2.7,
        "Rds": 0.032,
        "Coss": 155,
        "Ciss": 1750,
        "Crss": 40,
        "Qg": 26,
        "Qgd": 9,
        "Vgsth": 5,
        "RthJC": 1.045,
        "tr": 35,
        "tf": 20
    },
    
    "IRFB4019PBF": {
        "Vds": 150,
        "Rg": 2.4,
        "Rds": 0.080,
        "Coss": 74,
        "Ciss": 800,
        "Crss": 19,
        "Qg": 20,
        "Qgd": 4.1,
        "Vgsth": 4.9,
        "RthJC": 1.88,
        "tr": 13,
        "tf": 7.8
    },
    
    "IPP200N15N": {
        "Vds": 150,
        "Rg": 2.4,
        "Rds": 0.016,
        "Coss": 214,
        "Ciss": 1820,
        "Crss": 5,
        "Qg": 31,
        "Qgd": 4,
        "Vgsth": 3,
        "RthJC": 1.0,
        "tr": 11,
        "tf": 6
    },
    
    "TK32E12N1": {
        "Vds": 120,
        "Rg": 1.9,
        "Rds": 0.011,
        "Coss": 330,
        "Ciss": 2000,
        "Crss": 13,
        "Qg": 34,
        "Qgd": 9.8,
        "Vgsth": 4,
        "RthJC": 1.27,
        "tr": 14,
        "tf": 14
    },
    
    "IRFB4020PBF": {
        "Vds": 200,
        "Rg": 3.2,
        "Rds": 0.080,
        "Coss": 91,
        "Ciss": 1200,
        "Crss": 20,
        "Qg": 18,
        "Qgd": 5.3,
        "Vgsth": 4.9,
        "RthJC": 1.43,
        "tr": 12,
        "tf": 6.3
    },
    
    "GT150N12T": {
        "Vds": 120,
        "Rg": 3,
        "Rds": 0.018,
        "Coss": 180,
        "Ciss": 1650,
        "Crss": 5,
        "Qg": 25,
        "Qgd": 6,
        "Vgsth": 3.7,
        "RthJC": 1.3,
        "tr": 3,
        "tf": 3
    },
    
    "IRFB5615PBF": {
        "Vds": 150,
        "Rg": 2.7,
        "Rds": 0.032,
        "Coss": 155,
        "Ciss": 1750,
        "Crss": 40,
        "Qg": 26,
        "Qgd": 9,
        "Vgsth": 5,
        "RthJC": 1.045,
        "tr": 23.1,
        "tf": 13.1
    },    
    
    "RX2R03BBH": {
        "Vds": 150,
        "Rg": 0.9,
        "Rds": 0.029,
        "Coss": 180,
        "Ciss": 2150,
        "Crss": 13,
        "Qg": 37,
        "Qgd": 9.6,
        "Vgsth": 4,
        "RthJC": 2.40,
        "tr": 14,
        "tf": 22
    } 
    
}

# ==============================================================
# 4) UNIT CONVERSIONS FOR EACH MOSFET
# ==============================================================

def convert_units(p):
    """Convert units from datasheet formats to SI units."""
    return {
        "Vds":      p["Vds"],            # Volts - Drain-Source Voltage
        "Rds":      p["Rds"],            # Ohms - RDS(on)
        "Rg":       p["Rg"],             # Ohms - Internal Gate resistance
        "Coss":     p["Coss"] * 1e-12,   # pF → F - Output capacitance
        "Ciss":     p["Ciss"] * 1e-12,   # pF → F - Input capacitance
        "Crss":     p["Crss"] * 1e-12,   # pF → F - Reverse Transfer Capacitance
        "Qg":       p["Qg"] * 1e-9,      # nC → C - Total gate charge
        "Qgd":      p["Qgd"] * 1e-9,     # nC → C - Gate - Drain charge
        "Vplateau": p["Vgsth"] + 1.0,    # Volts - Approximation du plateau Miller
        "tr":       p["tr"] * 1e-9,      # ns → s - Rise time
        "tf":       p["tf"] * 1e-9,      # ns → s - Fall time
        "RthJC":    p["RthJC"]           # °C/W - Thermal resistance, junction - case
    }

# ==============================================================
# 5) COMPUTE LOSSES
# ==============================================================

rows = []

for name, raw in mosfets.items():
    p = convert_units(raw)
    
    tsw = p["tr"] + p["tf"]
    
    P_cond = p["Rds"] * Irms**2
    P_coss = 0.5 * p["Coss"] * Vds**2 * fsw_Hz
    P_sw   = 0.5 * Vds * Ipk * tsw * fsw_Hz
    P_gate = Vgs * p["Qg"] * fsw_Hz
    
    #R1_min, R1_max = compute_r1_simple(p["Qgd"], p["Vplateau"], p["Rg"])
    #print(f"{name}: Recommended R1 = {R1_min:.1f}–{R1_max:.1f} Ω")
    
    P_total = P_cond + P_coss + P_sw + P_gate
    Tj = Tamb + P_total * (p["RthJC"] + Rth_CS + Rth_SA)
    
    rows.append({
        "device": name,
        "P_cond_W": P_cond,
        "P_coss_W": P_coss,
        "P_sw_W": P_sw,
        "P_gate_W": P_gate,
        "P_total_W": P_total,
        "Tj_C": convert_temp(Tj)
    })

df = pd.DataFrame(rows)
df.to_csv("mosfet_losses.csv", index=False)

# ==============================================================
# 6) PLOT
# ==============================================================

labels = df["device"]
x = np.arange(len(labels))

cond = df["P_cond_W"]
coss = df["P_coss_W"]
sw   = df["P_sw_W"]
gate = df["P_gate_W"]
Tj   = df["Tj_C"]

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.set_ylabel("Power loss (W)")

ax1.bar(x, cond, label="Conduction", zorder=3)
ax1.bar(x, coss, bottom=cond, label="Coss", zorder=3)
ax1.bar(x, sw, bottom=cond+coss, label="Switching", zorder=3)
ax1.bar(x, gate, bottom=cond+coss+sw, label="Gate", zorder=3)

ax1.grid(True, axis="y", linestyle="--", alpha=0.5, zorder=0)
ax1.legend(loc="upper right")

# Expand top margin enough for title
plt.subplots_adjust(top=0.88)

fig.suptitle(
    "MOSFET losses and junction temperature (Tj)",
    fontweight="bold",
    fontsize=14,
    y=0.99
)

fig.text(
    0.5, 0.954,
    f"UC3845A Flyback {Vin}V→{Vout}V @ {Iout}A – Heatsink = {Rth_model} – Ta = {convert_temp(Tamb):.1f}°{TEMP_UNIT}",
    ha="center",
    va="center",
    fontsize=11,
)

ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=25, ha="right")

ax2 = ax1.twinx()
ax2.plot(x, Tj, "-o", color="red", linewidth=2)
ax2.set_ylabel(f"Junction Temp (°{TEMP_UNIT})", color="red")
ax2.set_ylim(min(Tj)-5, max(Tj)+10)

for i, tj in enumerate(Tj):
    ax2.text(i, tj + 1, f"{tj:.1f}°{TEMP_UNIT}",
             ha="center", color="red", fontweight="bold",
             path_effects=[path_effects.Stroke(linewidth=1, foreground="white"),
                           path_effects.Normal()])

# ==============================================================
# 7) ADD R1 RECOMMENDATION TO THE GRAPH
# ==============================================================

# Compute maximum bar height for normalization
max_bar = max((cond + coss + sw + gate))

for i, name in enumerate(labels):
    raw = mosfets[name]
    p = convert_units(raw)
    R1_min, R1_max = compute_r1_simple(p["Qgd"], p["tr"], p["tf"])

    r1_text = f"R1: {R1_min:.0f}–{R1_max:.0f}Ω"

    ax1.text(
        i,
        -0.02 * max_bar,         # small offset: −2% of total bar height
        r1_text,
        ha="center",
        va="top",
        fontsize=9,
        fontweight="bold",
        color="black",
        path_effects=[path_effects.Stroke(linewidth=1, foreground="white"),
                      path_effects.Normal()]
    )

# Expand bottom margin enough for R1 labels
ax1.set_ylim(bottom=-0.08 * max_bar)   # −8% instead of -20%


# ==============================================================
# 8) PLOT AND SAVE GRAPH
# ==============================================================

plt.tight_layout()
plt.savefig("Mosfet_thermal_plot.png", dpi=300)
plt.show()

