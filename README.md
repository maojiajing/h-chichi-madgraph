# h-chichi-madgraph

## 1. Change lifetime in lhe file

```
python ../../bin/internal/lhe_parser.py unweighted_events.lhe.gz unweighted_events_pl_1000.lhe 1000 
gzip unweighted_events_pl_1000.lhe
mv unweighted_events_pl_1000.lhe.gz unweighted_events.lhe.gz
```

## 2. Run Pythia8
```
./bin/madevent pythia8 run_01 --tag=pl_1000
```

## 3. Run Delphes

```
In directory /home/maojiajing/programs/h-chichi-madgraph/madgraph_output/LLP-test/gldgrv-h-bb-v2/Events/run_01
gunzip Events/run_01/pl_1000_pythia8_events.hepmc.gz
~/programs/h-chichi-madgraph$ ../delphes/DelphesHepMC /home/maojiajing/programs/delphes/cards/delphes_card_CMS.tcl  delphes_output/run_01_pl_1000.root madgraph_output/LLP-test/gldgrv-h-bb-v2/Events/run_01/pl_1000_pythia8_events.hepmc
```

## 4. Check lifetime



