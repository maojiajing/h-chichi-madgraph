python lhe_parser_n3n2.py /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/Events/n3n2-n1-hbb-hbb-0827-m127-evt1000/unweighted_events.lhe.gz /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/Events/n3n2-n1-hbb-hbb-0827-m127-evt1000/unweighted_events_pl1000.lhe 1000 
gzip /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/Events/n3n2-n1-hbb-hbb-0827-m127-evt1000/unweighted_events_pl1000.lhe 
mv /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/Events/n3n2-n1-hbb-hbb-0827-m127-evt1000/unweighted_events_pl1000.lhe /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/Events/n3n2-n1-hbb-hbb-0827-m127-evt1000/unweighted_events.lhe.gz 
cd /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827 
./bin/madevent pythia8 n3n2-n1-hbb-hbb-0827-m127-evt1000 --tag=pl_1000 
cd  
gunzip /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/Events/n3n2-n1-hbb-hbb-0827-m127-evt1000/pl_1000_pythia8_events.hepmc.gz 
./programs/delphes/DelphesHepMC /home/maojiajing/programs/delphes/cards/delphes_card_CMS.tcl /home/maojiajing/programs/delphes_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/n3n2-n1-hbb-hbb-0827-m127-evt1000.root /home/maojiajing/programs/madgraph_output/MSSM-1d-prod/n3n2-n1-hbb-hbb-0827/Events/n3n2-n1-hbb-hbb-0827-m127-evt1000/pl_1000_pythia8_events.hepmc 
cd /home/maojiajing/programs/h-chichi-madgraph 
