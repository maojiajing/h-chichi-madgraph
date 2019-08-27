import os, sys, argparse

# cmd parser
parser = argparse.ArgumentParser(description='make mass scan list') 
parser.add_argument('-i', '--inputDir', dest='dname', type=str, default=None, required=True)
parser.add_argument('-l', '--label', dest='name', type=str, default=None)
parser.add_argument('-o', '--output', dest='fname', type=str, default='output.txt')
parser.add_argument('-n', '--nevents', dest='evt', type=int, default=1000)
parser.add_argument('-b', '--begin', dest='begin', type=float, default=125)
parser.add_argument('-e', '--end', dest='end', type=float, default=500)
parser.add_argument('-s', '--step', dest='step', type=float, default=25)

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

if __name__ == "__main__":
        pwd = os.getcwd()
        out_n = pwd + '/' + output
        out_f = open(out_n, 'w')
        for mass_i in range(0, mass_n):
            #print('mass_i', mass_i)
            mass = mass_l + mass_i * mass_s
            if mass==125:
                mass =127
            label_n = label + '-m' + str(mass).replace('.0','') + '-evt' + str(nevt) 
            out_f.write('launch ' + inputDir + ' -n ' + label_n + ' \n')
            out_f.write('set nevents ' + str(nevt) + ' \n')
            out_f.write('set MNEU1 1' + ' \n')
            out_f.write('set MNEU2 ' + str(mass) + ' \n')
            out_f.write('set MNEU3 ' + str(mass) + ' \n')
        out_f.close()

