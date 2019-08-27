import os, sys, argparse

# cmd parser
parser = argparse.ArgumentParser(description='make mass scan list') 
parser.add_argument('-i', '--inputDir', dest='dname', type=str, default=None, required=True)
parser.add_argument('-l', '--label', dest='name', type=str, default=None)
parser.add_argument('-o', '--output', dest='fname', type=str, default='output.sh')
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
            out_f.write('cp lhe_parser_n3n2.py ' + inputDir + '/bin/internal/lhe_parser.py ' + ' \n')
            out_f.write('cd ' + inputDir + ' \n')
            out_f.write('python bin/internal/lhe_parser.py ' + lhe_in + ' ' + lhe_out + ' ' + str(int(pl)) + ' \n')
            out_f.write('gzip ' + lhe_out + ' \n')
            out_f.write('mv ' + lhe_out + ' ' + lhe_in + ' \n')
            out_f.write('cd ' + inputDir + ' \n')
            out_f.write('./bin/madevent pythia8 ' + label_n + ' --tag=pl_' + str(int(pl)) + ' \n')
            out_f.write('cd ' + ' \n')
            hepmc_out = run_dir + 'pl_'+str(int(pl))+'_pythia8_events.hepmc.gz'
            out_f.write('gunzip ' + hepmc_out + ' \n')
            del_out = delDir + '/' + label_n + '.root'
            out_f.write('./programs/delphes/DelphesHepMC ' +card + ' ' + del_out + ' ' + hepmc_out.replace('.gz','') + ' \n')
            out_f.write('cd ' + curDir + ' \n')
        out_f.close()

