#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
##!/mnt/lustre_fs/users/mjmcc/apps/python2.7/bin/python
# ----------------------------------------
# USAGE:

# ----------------------------------------
# PREAMBLE:

import sys
import numpy as np
import os
import matplotlib.pyplot as plt
from plotting_functions import *

# ----------------------------------------
# VARIABLE DECLARATION

descriptor = sys.argv[1]	# descriptor to decide which trajectory group to analyze for all systems
nResidue = int(sys.argv[2])
res_offset = int(sys.argv[3])

# description of constant_list.append and sys_list.append(['velocity number','equilibrated portion of the system for that specific velocity number'])
constant_list = []
constant_list.append(['wt_ssrna_atp','001.100'])

nCons = len(constant_list)

sys_list = []
#sys_list.append(['e285d_ssrna_atp','001.100'])
#sys_list.append(['a286l_ssrna_atp','001.100'])
#sys_list.append(['r387a_ssrna_atp','001.100'])
#sys_list.append(['r387m_ssrna_atp','001.100'])
sys_list.append(['s411a_ssrna_atp','001.100'])

nSys = len(sys_list)

first_residue = res_offset+1
residue_285 = res_offset+118+1
last_residue = res_offset+nResidue+1
print first_residue,residue_285,last_residue

res_highlight_list = [[(first_residue,last_residue),(first_residue,last_residue)]]

# ----------------------------------------
# SUBROUTINES:

# ----------------------------------------
# MAIN PROGRAM:

for i in range(nCons):
	avg1 = np.loadtxt('%s.%s_1.avg_distance_matrix.dat' %(constant_list[i][1],constant_list[i][0]))

	nRes = len(avg1)

	for j in range(nSys):
		avg2 = np.loadtxt('../../../../%s/velocity.1/md/res_res_COM_distance_matrix/%s.%s_1.avg_distance_matrix.dat' %(sys_list[j][0],sys_list[j][1],sys_list[j][0]))
#		std2 = np.loadtxt('../../../../%s/velocity.1/md/correlation_analysis/%s.%s_1.std_distance_matrix.dat' %(sys_list[j][0],sys_list[j][1],sys_list[j][0]))
		avg_data = avg1 - avg2
#		avg_data = np.abs(avg1) - np.abs(avg2)
		print 'for %s and %s: vmax %f vmin %f' %(constant_list[i][0],sys_list[j][0],np.amax(avg_data),np.amin(avg_data))
#		std_data = std1 - std2

		out1 = open('AVG_dist_matrix.%s.%s.hist.dat' %(constant_list[i][0],sys_list[j][0]),'w')
		out2 = open('AVG_dist_matrix.%s.%s.output' %(constant_list[i][0],sys_list[j][0]),'w')
		count_array = np.zeros(nRes)
		for x in range(nCons):
			for y in range(nRes):
				if abs(avg_data[x][y]) > 1.0:
					out1.write('%s   %s   %03d (%d)   %03d (%d)   %f\n' %(constant_list[i][0],sys_list[j][0],x+1,x+168,y+1,y+168,avg_data[x][y]))
					count_array[x] += 1
					count_array[y] += 1
		for x in range(nCons):
			out2.write('%03d   %03d   %d\n' %(x+1,x+168,count_array[x]))
		out1.close()
		out2.close()

		residue_range = np.array(range(first_residue,last_residue))
		print residue_range[0],residue_range[-1], len(residue_range)

		for i in range(len(res_highlight_list)):
			temp = plt.figure(figsize=(12,9))
			plt.pcolormesh(residue_range,residue_range,avg_data,cmap='bwr',vmin=-1.5,vmax=1.5)
			cb1 = plt.colorbar(cmap='bwr')
			cb1.set_label('Distance', size=14)
#			plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
			plt.title('Difference Distance between %s and %s' %(constant_list[i][0],sys_list[j][0]))
			plt.xlabel('Residue Number', size=14)
			plt.ylabel('Residue Number', size=14)
			plt.xlim(187,500)
			plt.ylim(187,500)
			plt.text(470,194, r'Motif I')
			plt.hlines(192,192,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.hlines(203,192,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(192,187,203,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(203,187,203,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.text(470,223, r'Motif Ia')
			plt.hlines(220,220,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.hlines(231,220,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(220,187,231,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(231,187,231,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.text(470,283, r'Motif II')
			plt.hlines(281,281,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.hlines(290,281,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(281,187,290,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(290,187,290,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.text(470,313, r'Motif III')
			plt.hlines(313,313,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.hlines(319,313,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(313,187,319,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(319,187,319,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.text(470,359, r'Motif IV')
			plt.hlines(358,358,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.hlines(365,358,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(358,187,365,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(365,187,365,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.text(470,384, r'Motif IVa')
			plt.hlines(382,382,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.hlines(391,382,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(382,187,391,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(391,187,391,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.text(470,407, r'Motif V')
			plt.hlines(403,403,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.hlines(417,403,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(403,187,417,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(417,187,417,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.text(470,458, r'Motif VI')
			plt.hlines(455,455,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.hlines(468,455,500,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(455,187,468,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.vlines(468,187,468,colors='k',linestyles='solid',label='',hold=None,data=None)
			plt.savefig('%s.%s.%s.difference_avg_dist_matrix.heatmap.png' %(descriptor,constant_list[i][0],sys_list[j][0]),dpi=300,transparent=True)
			plt.close()

