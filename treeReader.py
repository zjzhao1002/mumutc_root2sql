from array import array
from ROOT import TFile

class treeReader:
    def __init__(self, filename, treename):
        self.input_file = TFile(filename)
        self.tree = self.input_file.Get(treename)
    
    def nEvents(self):
        return self.tree.GetEntries()
    
    def getDATA(self):
        self.njets = array('i', [0])
        self.tree.SetBranchAddress('njets', self.njets)
        self.ptj1 = array('f', [0.0])
        self.tree.SetBranchAddress('ptj1', self.ptj1)
        self.ptj2 = array('f', [0.0])
        self.tree.SetBranchAddress('ptj2', self.ptj2)
        self.enerj1 = array('f', [0.0])
        self.tree.SetBranchAddress('enerj1', self.enerj1)
        self.enerj2 = array('f', [0.0])
        self.tree.SetBranchAddress('enerj2', self.enerj2)
        self.mjj = array('f', [0.0])
        self.tree.SetBranchAddress('mjj', self.mjj)
        self.mj1 = array('f', [0.0])
        self.tree.SetBranchAddress('mj1', self.mj1)
        self.mj2 = array('f', [0.0])
        self.tree.SetBranchAddress('mj2', self.mj2)
        self.hb = array('i', [0])
        self.tree.SetBranchAddress('hb',self.hb)
        self.lb = array('i', [0])
        self.tree.SetBranchAddress('lb',self.lb)
