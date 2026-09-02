import sys
import os
import traceback

print("Iniciando diagnóstico...")

try:
    print("Importando tkinter...")
    import tkinter as tk
    from tkinter import ttk
    print("Tkinter OK")
except Exception:
    traceback.print_exc()

try:
    print("Importando tkcalendar...")
    from tkcalendar import DateEntry
    print("tkcalendar OK")
except Exception:
    traceback.print_exc()

try:
    print("Importando matplotlib...")
    import matplotlib.pyplot as plt
    print("matplotlib OK")
except Exception:
    traceback.print_exc()

print("Importando módulos locales...")
try:
    from ui.tabs.planificacion import PlanificacionTab
    print("PlanificacionTab OK")
    from ui.tabs.entrenamientos import EntrenamientosTab
    print("EntrenamientosTab OK")
    from ui.tabs.asistencia import AsistenciaTab
    print("AsistenciaTab OK")
    from ui.tabs.comparativa import ComparativaTab
    print("ComparativaTab OK")
except Exception:
    traceback.print_exc()

print("Diagnóstico finalizado.")
