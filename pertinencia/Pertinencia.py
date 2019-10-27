import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe variables
#   Os atributos dos campões possuem um range entre [0, 10]

x_dan = np.arange(0, 11, 1)
x_res = np.arange(0, 11, 1)
x_con = np.arange(0, 11, 1)
x_mob = np.arange(0, 11, 1)
x_uti = np.arange(0, 11, 1)
x_alc = np.arange(0, 11, 1)

x_mag = np.arange(0, 6, 1)
x_tan = np.arange(0, 6, 1)
x_ass = np.arange(0, 6, 1)
x_lut = np.arange(0, 6, 1)
x_ati = np.arange(0, 6, 1)
x_sup = np.arange(0, 6, 1)

dan_b = fuzz.trimf(x_dan, [0, 0, 5])
dan_m = fuzz.trimf(x_dan, [0, 5, 10])
dan_a = fuzz.trimf(x_dan, [5, 10, 10])
res_b = fuzz.trimf(x_res, [0, 0, 5])
res_m = fuzz.trimf(x_res, [0, 5, 10])
res_a = fuzz.trimf(x_res, [5, 10, 10])
con_b = fuzz.trimf(x_con, [0, 0, 5])
con_m = fuzz.trimf(x_con, [0, 5, 10])
con_a = fuzz.trimf(x_con, [5, 10, 10])
mob_b = fuzz.trimf(x_mob, [0, 0, 5])
mob_m = fuzz.trimf(x_mob, [0, 5, 10])
mob_a = fuzz.trimf(x_mob, [5, 10, 10])
uti_b = fuzz.trimf(x_uti, [0, 0, 5])
uti_m = fuzz.trimf(x_uti, [0, 5, 10])
uti_a = fuzz.trimf(x_uti, [5, 10, 10])
alc_b = fuzz.trimf(x_alc, [0, 0, 5])
alc_m = fuzz.trimf(x_alc, [0, 5, 10])
alc_a = fuzz.trimf(x_alc, [5, 10, 10])

mag = fuzz.trimf(x_mag, [0, 0, 5])
tan = fuzz.trimf(x_tan, [0, 5, 10])
ass = fuzz.trimf(x_ass, [5, 10, 10])
lut = fuzz.trimf(x_lut, [10, 15, 15])
ati = fuzz.trimf(x_ati, [15, 20, 20])
sup = fuzz.trimf(x_sup, [20, 25, 25])


fig, ((ax0, ax1), (ax2, ax3), (ax4, ax5)) = plt.subplots(ncols=2, nrows=3, figsize=(15, 6))

ax0.plot(x_dan, dan_b, 'b', linewidth=1.5, label='baixo')
ax0.plot(x_dan, dan_m, 'g', linewidth=1.5, label='medio')
ax0.plot(x_dan, dan_a, 'r', linewidth=1.5, label='alto')
ax0.set_title('Dano do campeão')
ax0.legend()

ax1.plot(x_res, res_b, 'b', linewidth=1.5, label='Baixo')
ax1.plot(x_res, res_m, 'g', linewidth=1.5, label='Médio')
ax1.plot(x_res, res_a, 'r', linewidth=1.5, label='Alto')
ax1.set_title('Resistência do campeão')
ax1.legend()

ax2.plot(x_con, con_b, 'b', linewidth=1.5, label='Baixo')
ax2.plot(x_con, con_m, 'g', linewidth=1.5, label='Médio')
ax2.plot(x_con, con_a, 'r', linewidth=1.5, label='Alto')
ax2.set_title('Controle de grupo do campeão')
ax2.legend()

ax3.plot(x_mob, mob_b, 'b', linewidth=1.5, label='Baixo')
ax3.plot(x_mob, mob_m, 'g', linewidth=1.5, label='Médio')
ax3.plot(x_mob, mob_a, 'r', linewidth=1.5, label='Alto')
ax3.set_title('Mobilidade do campeão')
ax3.legend()

ax4.plot(x_uti, uti_b, 'b', linewidth=1.5, label='Baixo')
ax4.plot(x_uti, uti_m, 'g', linewidth=1.5, label='Médio')
ax4.plot(x_uti, uti_a, 'r', linewidth=1.5, label='Alto')
ax4.set_title('Utilidade do campeão')
ax4.legend()

ax5.plot(x_alc, alc_b, 'b', linewidth=1.5, label='Baixo')
ax5.plot(x_alc, alc_m, 'g', linewidth=1.5, label='Médio')
ax5.plot(x_alc, alc_a, 'r', linewidth=1.5, label='Alto')
ax5.set_title('Alcance do campeão')
ax5.legend()

for ax in (ax0, ax1, ax2, ax3, ax4, ax5):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.show()

fig, (ax6) = plt.subplots(nrows=1, figsize=(15, 6))

ax6.plot(x_mag, mag, 'r', linewidth=1.5, label='Mago')
ax6.plot(x_tan, tan, 'b', linewidth=1.5, label='Tanque')
ax6.plot(x_ass, ass, 'g', linewidth=1.5, label='Assassino')
ax6.plot(x_lut, lut, 'c', linewidth=1.5, label='Lutador')
ax6.plot(x_sup, sup, 'm', linewidth=1.5, label='Suporte')

ax6.spines['top'].set_visible(False)
ax6.spines['right'].set_visible(False)
ax6.get_xaxis().tick_bottom()
ax6.get_yaxis().tick_left()

plt.show()




