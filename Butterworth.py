import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
import warnings
import base64, tempfile

def get_embedded_icon():
    temp_icon = tempfile.NamedTemporaryFile(delete=False, suffix=".ico")
    temp_icon.write(base64.b64decode(ICON_DATA))
    temp_icon.close()
    return temp_icon.name
ICON_DATA = b"""AAABAAEAICAAAAEAIACoEAAAFgAAA
CgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAA
AACgAAAAwAAAAMAAAADAAAAAwAAAAMAAAADAAAAAwAAAAJAAAAAAAAAAAAAAAAAAAAAAAAAAkAAAAMAAAADAAAAAwAAAAMAAAADAAAAAwAAAAMAAAACgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAABMAAACpAAAAyAAAAMYAAADGAAAAxgAAAMYAAADGAAAAyQAAAJAAAAAFAAAAAAAAAAAAAAAFAAAAjgAAAMkAAADGAAAAxgAAAMYAAADGAAAAxgAAAMgAAACpAAAAEwAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGQAAANoAAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAArwAAAAQAAAAAAAAAAAAAAAIAAACoAAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAANoAA
AAZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZAAAA2gAAAP4AAADuAAAA6QAAAOkAAADpAAAA6QAAAPkAAAChAAAAAAAAAAAAAAAAAAAAAAAAAJUAAAD5AAAA6QAAAOkAAADpAAAA6Q
AAAO4AAAD+AAAA2gAAABkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABoAAADJAAAAdgAAADAAAAApAAAAKQAAACYAAAApAAAArAAAAJcAAAAAAAAAAAAAAAAAAAAAAAAAhQAAALYAAAA
qAAAAJgAAACkAAAApAAAALwAAAHQAAADKAAAAGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGgAAAIEAAAAIAAAAAAAAAAAAAAAEAAAAPwAAAJoAAADjAAAAeAAAAAAAAAAAAAAAAAAA
AAAAAABiAAAA4wAAAJkAAAA8AAAABAAAAAAAAAAAAAAACQAAAIEAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAEwAAAAAAAAAAAAAAFAAAAI4AAADyAAAA4QAAAGYAAAAQA
AAAAAAAAAAAAAAAAAAAAAAAAAsAAABRAAAA0AAAAPEAAACRAAAAGAAAAAAAAAAAAAAAEgAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYAAACpAAAA/wAAAO
QAAABCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArAAAA0QAAAP8AAACyAAAAGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHAAA
AlQAAAP8AAAD/AAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbAAAA+QAAAP8AAACcAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAEoAAADzAAAA/wAAAOsAAAAxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABUAAADPAAAA/wAAAPUAAABPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAADAAAAowAAAP8AAAD/AAAAxQAAAA0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJwAAAD/AAAA/wAAAKkAAAAFAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABkAAADYAAAA/wAAAP8AAACgAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeAAAAP8AAAD/AAAA3QA
AAB4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALwAAAO0AAAD/AAAA/wAAAIkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABm
AAAA/wAAAP8AAADyAAAAOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5AAAA8wAAAP8AAAD/AAAAgQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAGEAAAD/AAAA/wAAAPgAAABEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADIAAADvAAAA/wAAAP8AAACJAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAawAAAP8AAAD/AAAA9gAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHAAAANsAAAD/AAAA/wAAAKMAAAABAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACGAAAA/wAAAP8AAADpAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAqgAAAP8AAAD/AAAA
zQAAABMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwAAALQAAAD/AAAA/wAAAMQAAAAOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
ABUAAAA9wAAAP8AAAD0AAAASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuAAAA5wAAAP8AAAD/AAAAdgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAsAAACnAAAA/wAAAP8AAACuAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAJAAAAD/AAAA/wAAAMsAAAAcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACUAAADHAAAA/wAAAPkAAAB1AAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAABhAAAA8QAAAP8AAADiAAAARAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACsAAAC6AAAA/gAAAPIAAAB9AAAAEwAAAAAAAAAAAAAAAAAAAAAAAAARAAAAdAAAAO0AAAD/AAAA1QAAAEcAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYAAAB6AAAA2gAAAPoAAADMAAAAhAAAAF4AAABeAAAAggAAAMoAAAD7AAAA5wAAAJ
UAAAAmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAeAAAAWwAAAJUAAAC3AAAAwgAAAMMAAAC8AAA
AnwAAAGoAAAArAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUA
AAALAAAADAAAAAcAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAA//////////////////////ADwA/wAYAP8AGAD/ADwA/wA8AP8YPBj/MDwM/+D/B//B/4P/wf+D/4H/wf+B/8H/g//B/4P/wf+D/8H/gf/B/4H/gf/B/4P/wP8D/+B+B//wPA//+AAf//wAP///
wf//////////////////////8=
"""
def butterworth_g_values(n):
    if n < 1:
        raise ValueError("Order n must be >= 1")
    g = [2.0 * np.sin((2*k - 1) * np.pi / (2.0 * n)) for k in range(1, n + 1)]
    return np.array(g, dtype=float)

def scale_to_LC_with_type(g_vals, fc, Z0, filter_type='LP'):
    omega_c = 2 * np.pi * fc
    Ls = []
    Cs = []
    for i, g in enumerate(g_vals, start=1):
        if filter_type.upper() == 'LP':
            if i % 2 == 1:
                Ls.append(Z0 * g / omega_c)
                Cs.append(None)
            else:
                Ls.append(None)
                Cs.append(g / (Z0 * omega_c))
        elif filter_type.upper() == 'HP':
            if i % 2 == 1:
                Ls.append(None)
                Cs.append(1 / (Z0 * g * omega_c))
            else:
                Ls.append(Z0 * g / omega_c)
                Cs.append(None)
        else:
            raise ValueError("filter_type must be 'LP' or 'HP'")
    return Ls, Cs

def eff_eps(eps_r, w_h):
    if w_h <= 0:
        return (eps_r + 1.0)/2.0
    if w_h <= 1.0:
        F = (eps_r - 1.0)/(2*np.sqrt(1+12/w_h)) + 0.04*(1-w_h)**2
    else:
        F = (eps_r - 1.0)/(2*np.sqrt(1+12/w_h))
    return (eps_r + 1.0)/2.0 + F

def z0_from_wh(eps_r, w_h):
    eps_eff = eff_eps(eps_r, w_h)
    if w_h <= 1.0:
        z0 = 60 / np.sqrt(eps_eff) * np.log(8/w_h + 0.25*w_h)
    else:
        z0 = 120*np.pi / (np.sqrt(eps_eff)*(w_h + 1.393 + 0.667*np.log(w_h+1.444)))
    return z0

def wh_from_z0(eps_r, Z0_target, h, tol=1e-6, max_iter=80):
    a, b = 1e-6, 100.0
    za = z0_from_wh(eps_r, a) - Z0_target
    zb = z0_from_wh(eps_r, b) - Z0_target
    if za*zb > 0:
        warnings.warn(f"Z0={Z0_target} out of solver bounds; returning W/h={a}")
        return a*h
    for _ in range(max_iter):
        m = 0.5*(a+b)
        zm = z0_from_wh(eps_r, m) - Z0_target
        if abs(zm)<tol:
            return m*h
        if za*zm<0:
            b, zb = m, zm
        else:
            a, za = m, zm
    warnings.warn("wh_from_z0: max iterations reached; returning mid-point")
    return 0.5*(a+b)*h

def L_C_to_Zs_Zp(Ls, Cs, fc, theta_rad):
    omega = 2*np.pi*fc
    Zs, Zp = [], []
    for L, C in zip(Ls, Cs):
        if L is not None:
            Zs.append(L*omega/theta_rad)
            Zp.append(None)
        elif C is not None:
            Zp.append(theta_rad/(C*omega))
            Zs.append(None)
        else:
            Zs.append(None)
            Zp.append(None)
    return Zs, Zp

def ABCD_series(Z):
    return np.array([[1,Z],[0,1]],dtype=complex)

def ABCD_shunt(Y):
    return np.array([[1,0],[Y,1]],dtype=complex)

def cascade_ABCD_list(list_ABCD):
    M = np.eye(2,dtype=complex)
    for A in list_ABCD:
        M = M @ A
    return M

def ABCD_to_S(M, Z0):
    A,B,C,D = M[0,0], M[0,1], M[1,0], M[1,1]
    denom = A + B/Z0 + C*Z0 + D
    if denom==0:
        return 0+0j,0+0j
    s11 = (A + B/Z0 - C*Z0 - D)/denom
    s21 = 2/denom
    return s11,s21

def lumped_network_s21(Ls,Cs,freqs,Z0,filter_type='LP'):
    s21 = np.zeros_like(freqs,dtype=complex)
    for idx,f in enumerate(freqs):
        omega = 2*np.pi*f
        ABCDs=[]
        for L,C in zip(Ls,Cs):
            if filter_type.upper()=='LP':
                if L is not None:
                    ABCDs.append(ABCD_series(1j*omega*L))
                if C is not None:
                    ABCDs.append(ABCD_shunt(1j*omega*C))
            elif filter_type.upper()=='HP':
                if C is not None:
                    ABCDs.append(ABCD_series(1/(1j*omega*C)))
                if L is not None:
                    ABCDs.append(ABCD_shunt(1/(1j*omega*L)))
        M = cascade_ABCD_list(ABCDs)
        _, s21[idx] = ABCD_to_S(M,Z0)
    return s21

def design_butterworth_microstrip(order, fc, Z0, substrate, theta_deg=20, filter_type='LP'):
    theta_rad = theta_deg*np.pi/180
    g = butterworth_g_values(order)
    Ls,Cs = scale_to_LC_with_type(g,fc,Z0,filter_type)
    Zs,Zp = L_C_to_Zs_Zp(Ls,Cs,fc,theta_rad)

    Ws,lengths=[],[]
    for Zs_i,Zp_i in zip(Zs,Zp):
        Z = Zs_i if Zs_i is not None else Zp_i
        if Z is not None:
            W = wh_from_z0(substrate['eps_r'], Z, substrate['h'])
            eps_eff_val = eff_eps(substrate['eps_r'], W/substrate['h'])
            lambda_g = 3e8/(fc*np.sqrt(eps_eff_val))
            ell = theta_rad/(2*np.pi)*lambda_g
            Ws.append(W)
            lengths.append(ell)
        else:
            Ws.append(None)
            lengths.append(None)

    freqs = np.linspace(fc*0.01, fc*6.0, 2000)
    s21 = lumped_network_s21(Ls,Cs,freqs,Z0,filter_type)

    return {
        'g': g,'Ls':Ls,'Cs':Cs,'Zs':Zs,'Zp':Zp,
        'Ws':Ws,'lengths':lengths,
        'freqs':freqs,'s21':s21,'filter_type':filter_type.upper()
    }

def print_design_summary(order, fc, Z0, substrate, theta_deg, Ls,Cs,Zs,Zp,Ws,lengths,filter_type):

    output_text.insert(tk.END, "==== Butterworth Stepped-Impedance Microstrip Design ====\n")
    output_text.insert(tk.END, f"Order={order}, fc={fc/1e9:.3f}GHz, Z0={Z0}Ω, Type={filter_type.upper()}\n")
    output_text.insert(tk.END, f"Substrate: eps_r={substrate['eps_r']}, h={substrate['h']*1e3:.3f} mm\n")
    output_text.insert(tk.END, f"Electrical length per section at fc: {theta_deg} deg\n")
    output_text.insert(tk.END, "Idx | Element | Value | Z_line(Ω) | W(mm) | Length(mm)\n")
    output_text.insert(tk.END, "====+==========+=============+===========+=========+=========\n")
    for i,(L,C,Zs_i,Zp_i,W,ell) in enumerate(zip(Ls,Cs,Zs,Zp,Ws,lengths),1):
        if filter_type.upper()=='LP':
            if L is not None:
                typ='Series L'; val=f"{L:.3e} H"
            else:
                typ='Shunt C'; val=f"{C:.3e} F"
        else:
            if C is not None: typ='Series C'; val=f"{C:.3e} F"
            elif L is not None: typ='Shunt L'; val=f"{L:.3e} H"
            else: typ='Elem'; val='N/A'
        Zline = f"{Zs_i:.2f}" if Zs_i is not None else (f"{Zp_i:.2f}" if Zp_i is not None else "N/A")
        Wmm = f"{W*1e3:.3f}" if W is not None else "N/A"
        ellmm = f"{ell*1e3:.3f}" if ell is not None else "N/A"
        output_text.insert(tk.END, f"{i:3d} | {typ:8s} | {val:10s} | {Zline:9s} | {Wmm:7s} | {ellmm:9s}\n")
    output_text.insert(tk.END, "=============================================================\n")
    output_text.see(tk.END)

def design_filter():
    try:
        order = int(order_entry.get())
        fc = float(fc_entry.get())
        Z0 = float(Z0_entry.get())
        eps_r = float(epsr_entry.get())
        h = float(h_entry.get())
        theta_deg = float(theta_entry.get())
        filter_type = filter_type_var.get()
        substrate = {'eps_r': eps_r, 'h': h}

        design = design_butterworth_microstrip(order, fc, Z0, substrate, theta_deg, filter_type)

        print_design_summary(order, fc, Z0, substrate, theta_deg,
                             design['Ls'], design['Cs'],
                             design['Zs'], design['Zp'],
                             design['Ws'], design['lengths'],
                             design['filter_type'])

        plt.figure(figsize=(9,4))
        plt.gcf().canvas.manager.window.iconbitmap(get_embedded_icon())
        plt.plot(design['freqs']/1e9, 20*np.log10(np.abs(design['s21'])), label='|S21| dB')
        plt.axvline(fc/1e9,color='k',linestyle='--',label='fc')
        plt.title(f"Stepped-Impedance Butterworth {design['filter_type']} Filter (order {order})")
        plt.xlabel("Frequency (GHz)")
        plt.ylabel("S21 (dB)")
        ymin = np.min(20*np.log10(np.abs(design['s21'])+1e-12))
        plt.ylim(max(ymin-10,-120),2)
        plt.grid(True,ls='--',lw=0.4)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
#===============================================================================================
def clear_output():
    output_text.delete(1.0, tk.END)

root = tk.Tk()
root.title("Butterworth Microstrip Filter Designer")
root.iconbitmap(get_embedded_icon())

tk.Label(root, text="Filter Order:").grid(row=0, column=0, sticky="e")
order_entry = tk.Entry(root); order_entry.grid(row=0, column=1); order_entry.insert(0, "5")

tk.Label(root, text="Cutoff Frequency (Hz):").grid(row=1, column=0, sticky="e")
fc_entry = tk.Entry(root); fc_entry.grid(row=1, column=1); fc_entry.insert(0, "2.4e9")

tk.Label(root, text="Characteristic Impedance (Ohms):").grid(row=2, column=0, sticky="e")
Z0_entry = tk.Entry(root); Z0_entry.grid(row=2, column=1); Z0_entry.insert(0, "50")

tk.Label(root, text="Substrate eps_r:").grid(row=3, column=0, sticky="e")
epsr_entry = tk.Entry(root); epsr_entry.grid(row=3, column=1); epsr_entry.insert(0, "4.4")

tk.Label(root, text="Substrate h (m):").grid(row=4, column=0, sticky="e")
h_entry = tk.Entry(root); h_entry.grid(row=4, column=1); h_entry.insert(0, "0.0016")

tk.Label(root, text="Theta (deg):").grid(row=5, column=0, sticky="e")
theta_entry = tk.Entry(root); theta_entry.grid(row=5, column=1); theta_entry.insert(0, "15")

tk.Label(root, text="Filter Type:").grid(row=6, column=0, sticky="e")
filter_type_var = tk.StringVar(value="HP")
filter_type_menu = ttk.Combobox(root, textvariable=filter_type_var, values=["LP", "HP"], state="readonly")
filter_type_menu.grid(row=6, column=1)

clear_button = tk.Button(root, text="Clear Text", command=clear_output)
clear_button.grid(row=9, column=0, columnspan=2, pady=5)
design_button = tk.Button(root, text="Design Filter", command=design_filter)
design_button.grid(row=7, column=0, columnspan=2, pady=10)
output_text = tk.Text(root, width=80, height=20)
output_text.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()