cp lhe_parser_n3n2.py /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/bin/internal/lhe_parser.py  
cd /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827 
python bin/internal/lhe_parser.py /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/Events/n3n2-n1-hbb-hbb-0827-m150-evt1000/unweighted_events.lhe.gz /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/Events/n3n2-n1-hbb-hbb-0827-m150-evt1000/unweighted_events_pl1000.lhe 1000 
scp /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/Events/n3n2-n1-hbb-hbb-0827-m150-evt1000/unweighted_events_pl1000.lhe jmao@login-1.hep.caltech.edu:/data/jmao/LHE/m150_pl1000.lhe 
cd /home/maojiajing/programs/h-chichi-madgraph 
