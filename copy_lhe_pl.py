import os, sys, argparse

# cmd parser
parser = argparse.ArgumentParser(description='make mass scan list') 
parser.add_argument('-i', '--inputDir', dest='dname', type=str, default=None, required=True)
parser.add_argument('-l', '--label', dest='name', type=str, default=None)
parser.add_argument('-o', '--output', dest='fname', type=str, default='copy.sh')
parser.add_argument('-n', '--nevents', dest='evt', type=int, default=1000)
parser.add_argument('-b', '--begin', dest='begin', type=float, default=125)
parser.add_argument('-e', '--end', dest='end', type=float, default=500)
parser.add_argument('-s', '--step', dest='step', type=float, default=25)
parser.add_argument('-pl', '--ctau', dest='ctau', type=float, default=0.1)

opt = parser.parse_args()

inputDir = opt.dname
label = opt.name
output = opt.fname
nevt = opt.evt
mass_l = opt.begin
mass_h = opt.end
mass_s = opt.step
mass_n = int((mass_h - mass_l)/mass_s)
#print('mass_n', mass_n)
pl = opt.ctau

card='/home/maojiajing/programs/delphes/cards/delphes_card_CMS.tcl'
delDir=inputDir.replace('madgraph','delphes')
t2_dir='/data/jmao/LHE/'

if __name__ == "__main__":
        pwd = os.getcwd()
        curDir = pwd
        out_n = pwd + '/' + output
        out_f = open(out_n, 'w')
        for mass_i in range(0, mass_n):
            #print('mass_i', mass_i)
            mass = mass_l + mass_i * mass_s
            if mass==125:
                mass =127
            label_n = label + '-m' + str(mass).replace('.0','') + '-evt' + str(nevt) 
            run_dir = inputDir + '/Events/' + label_n + '/'
            lhe_in = run_dir + 'unweighted_events.lhe.gz'
            lhe_out = run_dir + 'unweighted_events_pl'+str(int(pl))+'.lhe'
            lhe_pl_out = t2_dir + 'm' + str(int(mass)) + '_pl'+str(int(pl))+'.lhe'
            out_f.write('gfal-copy ' + lhe_pl_out + ' gsiftp://transfer.ultralight.org//store/group/phys_exotica/jmao/aodsim/RunIISummer16/LHE/MSSM-1d-prod/n3n2-n1-hbb-hbb/' + ' \n')
        out_f.close()

