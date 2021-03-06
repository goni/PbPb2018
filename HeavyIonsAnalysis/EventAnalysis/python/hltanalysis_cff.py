import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi import *

hltbitanalysis.UseTFileService = cms.untracked.bool(True)
hltanalysis = hltbitanalysis.clone(
    l1GtReadoutRecord    = cms.InputTag("gtDigis"),
    l1GctHFBitCounts     = cms.InputTag("gctDigis"),
    l1GctHFRingSums      = cms.InputTag("gctDigis"),
    l1extramu            = cms.string('l1extraParticles'),
    l1extramc            = cms.string('l1extraParticles'),
    hltresults           = cms.InputTag("TriggerResults","","HLT"),
    dummyBranches = cms.untracked.vstring()
    )


hltanalysisReco = hltbitanalysis.clone(
    l1tAlgBlkInputTag               = cms.InputTag("gtStage2Digis"),
    l1tExtBlkInputTag               = cms.InputTag("gtStage2Digis"),
    gObjectMapRecord                = cms.InputTag("gtStage2ObjectMap"),
    gmtStage2Digis                  = cms.string("gmtStage2Digis"),
    caloStage2Digis                 = cms.string("caloStage2Digis"),
    hltresults           = cms.InputTag("TriggerResults::HLT"),
)


skimanalysis = cms.EDAnalyzer("FilterAnalyzer",
                              hltresults = cms.InputTag("TriggerResults","","HiForest"),
                              superFilters = cms.vstring("")
)




