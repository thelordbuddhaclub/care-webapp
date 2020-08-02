import pickle
ls_image = [([-0.14993387,  0.07147986,  0.03987267, -0.02327273, -0.012801,
                   -0.00216479, -0.02125976, -0.02633528,  0.19820827, -0.14920695,
                   0.16940755, -0.02381077, -0.16188712, -0.09489044, -0.03789385,
                   0.02050179, -0.1112743, -0.15269099, -0.00412711, -0.06784474,
                   0.05247861, -0.01878699, -0.02142162,  0.05346927, -0.14125896,
                   -0.34354454, -0.07800335, -0.12489081,  0.05881725, -0.09283973,
                   -0.04425328,  0.04600906, -0.2047646, -0.05970973, -0.04811222,
                   0.07397509,  0.06094309,  0.06196084,  0.15042864, -0.00454803,
                   -0.10665448, -0.05050457,  0.0067315,  0.30604461,  0.16001736,
                   0.08267885, -0.04084636,  0.0211148,  0.10290729, -0.21498016,
                   0.02367281,  0.14659396,  0.12696341,  0.06453433,  0.05294429,
                   -0.09633879,  0.03363894,  0.02396532, -0.20534578,  0.10759358,
                   -0.01804812, -0.07146091,  0.04158381,  0.05057248,  0.26005051,
                   0.06154027, -0.05371091, -0.12443221,  0.17016429, -0.23392658,
                   0.03037927,  0.05756045, -0.04211013, -0.17372765, -0.17146099,
                   0.09477272,  0.37444881,  0.23673847, -0.11718253,  0.12451027,
                   -0.13441487, -0.11355262,  0.07315876,  0.02818773, -0.09624636,
                   0.07970645, -0.09075673,  0.02764656,  0.21844395,  0.05144849,
                   -0.02110951,  0.20672117, -0.01005914,  0.02948757,  0.07381564,
                   -0.05853487, -0.10982202,  0.02035322, -0.12471391, -0.00656888,
                   -0.02362333, -0.09934775,  0.03011237,  0.06460049, -0.16631828,
                   0.11662396, -0.03376886, -0.0353292, -0.05388442,  0.10082171,
                   -0.12561928, -0.09385061,  0.11252709, -0.25464627,  0.15779158,
                   0.13349134,  0.08838566,  0.19857308,  0.0722106,  0.0509987,
                   0.073975, -0.00581824, -0.04700017, -0.07569691,  0.04163749,
                   -0.0564715,  0.09370753,  0.03210698])]
ls_c_id = ['random']
with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(ls_image, f)

with open('dataset_c_ids.dat', 'wb') as f:
    pickle.dump(ls_c_id, f)
