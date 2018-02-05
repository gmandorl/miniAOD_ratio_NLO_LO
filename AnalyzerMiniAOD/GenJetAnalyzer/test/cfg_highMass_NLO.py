import FWCore.ParameterSet.Config as cms

processName = "JetStudy"
process = cms.Process(processName)


process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/g/gimandor/private/Hmumu/DY_check_MiniAOD/DY_M-50_LO_MiniAOD.root"))
    #fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/g/gimandor/private/Hmumu/DY_check_MiniAOD/DY_M-50_NLO_MiniAOD.root"))
    #fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/g/gimandor/private/Hmumu/DY_check_MiniAOD/DY_M-50_NLO_MiniAOD_2.root"))  # NLO
    fileNames = cms.untracked.vstring(
        ###--------------------------------------------------------------------------------------------------------------------------------------------- INCLUSIVE DY NLO highMass
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/B2D224D1-DDB3-E711-8A65-90B11CBCFFEA.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/B440EA8B-B1B3-E711-B357-008CFAC93D60.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/B681B9C5-E7B3-E711-8E6A-FA163E76F348.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/B6E4F103-78B3-E711-9CCE-008CFAC93EC4.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/B8048C9A-33B9-E711-A3A3-001E6757E05C.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/B8994B9E-1BB5-E711-8D13-549F35AD8BC9.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/B8CBAB5C-A0C6-E711-A5C1-4C79BA1812C1.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/BA5905B3-EAC8-E711-AB94-001E67A42BA2.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/BAB68B90-B7B3-E711-8BDB-0025904C7F70.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/BAD5C123-BBB3-E711-8E9D-008CFAED6FE8.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/BE0858C6-82B3-E711-ABA2-008CFAE45350.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/BE4549F2-2EBC-E711-8738-008CFAF71FB4.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/BEF9D745-ABB3-E711-B70B-008CFA197C3C.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/C08E4331-F4B8-E711-8C11-001E67792882.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/C2E00912-71B9-E711-85C4-10983627C3C1.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/C4480D49-91B3-E711-8AFF-008CFAC91E88.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/C498C140-5FBC-E711-A72E-008CFAF07728.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/C6B247CD-94B7-E711-9E0D-FA163EFF7E43.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/C6DC8680-C6B4-E711-B590-D4AE5269F656.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/C6F9A434-70BC-E711-AFDA-0025905C53D0.root',
       #####'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/C820CFD4-0CB9-E711-84B8-001E673966B2.root'
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/C825B031-5DB7-E711-8D37-008CFAE450E4.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/C85A5D46-B5B3-E711-BB97-008CFAE4541C.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/CA6A453F-CBB4-E711-8558-008CFA165F34.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/CE1AA77B-D9B3-E711-B43C-90B11CBCFFEA.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/CE26892F-97B3-E711-A174-008CFAC93BFC.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/CE54E81A-F6C7-E711-984D-0023AEEEB3EE.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/CE879586-CEC6-E711-9324-1866DA85DC9B.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/CEF7213F-EBB8-E711-9BA6-001E673966B2.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/D00F4EA6-93B3-E711-B549-008CFAC91E88.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/D0CEB780-03B4-E711-96CB-0CC47AA9906E.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/150000/D279ED39-D6B3-E711-9A6E-008CFAC942F0.root'
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/04D2221B-44B4-E711-8C81-FA163E1F2E98.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/06018525-B5B4-E711-A3E6-008CFAC91974.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/0651E2AA-47B8-E711-82EA-00E081CB65B2.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/0667D72A-41B6-E711-B917-A0369FC5252C.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/0A466FC7-76C8-E711-9D9E-90B11C1DBFB4.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/0CA7A773-07B9-E711-AB3B-901B0E542962.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/12AFD217-77C6-E711-B37A-0025905B856C.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/14E85CCC-4BB9-E711-B48E-001E675045FD.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/1A9E1692-F2B8-E711-B043-0CC47A5FC619.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/1AF6C4F1-A4B9-E711-BBAB-6C3BE5B52368.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/1CA50A77-1FB9-E711-87C4-0025905B85B2.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/2078DF60-90B7-E711-A2DD-F01FAFD9CF48.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/26F4978F-57B9-E711-B401-001E675045FD.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/2AE91793-1CB4-E711-9557-0CC47A4DED94.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/2C188FF0-90BC-E711-ACE3-001E67792514.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/2CF6EC7C-3AC8-E711-807A-7845C4FC397A.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/2CF7BC96-3CBD-E711-A2B6-A0369FC51E74.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/2E240421-2CB9-E711-8AFE-002590E7DE20.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/3296D791-87BC-E711-A16E-001E67792600.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/32D4E822-46C8-E711-BADB-001E67A404B5.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/32F4D39A-77C8-E711-AB12-549F3525BF58.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/34198DC0-16BF-E711-9D6A-008CFA1CB73C.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/3445669A-1EBA-E711-899E-F01FAFDC596D.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/34AACA43-07B4-E711-B9C4-0CC47A57CBCC.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/3C926C49-33B9-E711-AB35-20CF3019DF08.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/3CA1AB63-90C6-E711-8C63-44A84225C7BB.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/3CD2321B-58C6-E711-B334-1CB72C1B649A.root',
       ###########'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/42F1E033-1AB4-E711-89F9-003048F5E840.root'
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/5032C22B-67E4-E711-9438-02163E019B8F.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/580E29AE-84E5-E711-A20C-441EA158FECC.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/9A93AF7D-6DE4-E711-9C97-02163E01A687.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/B0F23712-26E5-E711-90CD-FA163E78B0FE.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/B2A6C533-75E5-E711-A4A2-02163E019C58.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/B665FB4E-20E5-E711-9DAF-00266CF2EBAC.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/BECE271C-83E5-E711-8ED6-008CFA111348.root'
       ########'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/C2AC6073-5DE4-E711-B0B1-02163E014604.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/D07F5006-9AE4-E711-B956-02163E01211B.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/D0A1CE29-B1EB-E711-88C0-C81F66B782DC.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/D25851EE-E5ED-E711-BDFE-A0369F83628A.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/D2BEA039-E9E4-E711-B9C1-00238BBD7672.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/D2C95EAD-67E8-E711-80F8-02163E0133BC.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/D2F4AABE-71E7-E711-A057-02163E0133AE.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/D4DF14B9-C4E8-E711-8F95-02163E014178.root'
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/DC36924B-97E8-E711-85E0-02163E01A750.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E0DEE272-7BEF-E711-8760-7CD30AD0A354.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E0E1D29E-DCE7-E711-9FAE-02163E014726.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E0E6522D-6FEC-E711-AD61-FA163E021FEE.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E49DF8F7-08E6-E711-81A2-0242AC1C0500.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E4B8CE1E-30ED-E711-8896-0025905B8610.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E4DC07DD-B1EB-E711-A36F-0CC47AD99144.root',
       ######'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E4E350A9-D7E5-E711-9523-4C79BA180A67.root'
       ######'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E4E8D5E6-E6EB-E711-830C-B499BAABD8C6.root',
       ######'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E6FB965C-F6E5-E711-BDE7-02163E019CE9.root',
       ######'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E8579244-F9E7-E711-B684-02163E019DAD.root'
#        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/EA24A3A9-9AE8-E711-A003-02163E011A23.root',
#        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/EA4BC011-85E8-E711-AD11-02163E01347B.root',
#        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/EA9EBD18-A1E8-E711-B31F-02163E011F8D.root',
#        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/EC71E5FF-B6E4-E711-9BF3-00215AA62C2A.root',
#        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/ECDAC668-33E7-E711-B2A0-008CFA1974CC.root',
#        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/F0E7CEBF-D1EC-E711-8694-002590FC5AD0.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/F2AC1866-E3E7-E711-9B6D-02163E014511.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/F2CCF836-EAE7-E711-BCF4-02163E0121D6.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/F6DE18BB-B5E9-E711-AE5C-0CC47A7E68AA.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/F6EF67FA-A8E8-E711-B71F-02163E019E2D.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/F87FD50C-A1E8-E711-9BD0-02163E01396A.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/F8BA1310-8EE8-E711-9669-02163E0134E1.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/FA063253-BDEB-E711-91B7-0CC47AD99112.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/FAB14BAD-B8E5-E711-B0C1-EC0D9A0B3060.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/FC1F1B59-78EF-E711-BC32-0425C5DE7BF6.root',
       #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/FE49E649-DAEB-E711-B5FE-0242AC130002.root'
       #####'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/FEF078A5-9DE8-E711-803C-02163E011B0D.root'
        ###--------------------------------------------------------------------------------------------------------------------------------------------- INCLUSIVE DY LO highMass
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/4CAA5BFF-C4E1-E711-A08D-F01FAFD690C9.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/54D9A68C-44DA-E711-838C-FA163E8CD4FA.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/54DB007E-36D7-E711-8502-02163E0135E2.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/5631EEFB-31D7-E711-9C15-02163E013940.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/567D439D-0EE5-E711-97F5-008CFAC91274.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/56A47497-1FD7-E711-AA51-02163E019E8F.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/5C4485B8-24D7-E711-8F66-02163E0140F3.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/5CDFD18F-1FD7-E711-BE99-02163E0140F1.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/5ED7A44E-5AD9-E711-94A9-EC0D9A0B3300.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/60DB4E17-D5E5-E711-8E33-A0369FC4CD54.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/629BFFC1-2FD7-E711-AE83-02163E01A1F7.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/6647FDEC-1FD7-E711-B248-02163E01A1E8.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/6810F975-0BD8-E711-9098-3417EBE528B2.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/681B6779-71D7-E711-A180-02163E01A37B.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/6A1F9D29-35D7-E711-A836-02163E01A2F2.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/6AE01785-25D7-E711-ABEB-02163E0134FA.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/701E0FD4-DAE2-E711-9A48-4C79BA1812C1.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/7813E9AE-3ED7-E711-8A3E-02163E014637.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/78B2AA9F-0FE2-E711-BEFE-5065F37D6152.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/7AD0EBC0-1FD7-E711-9E04-02163E01A3D3.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/7C2B6631-41D7-E711-88F0-02163E01A3BE.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/8014C683-F8E4-E711-B5A6-24BE05BD0F81.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/8021AAC8-2FD7-E711-928C-02163E01372E.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/82C30684-15E5-E711-A1D1-008CFA111348.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/848C09BE-12E5-E711-B62D-008CFAC9404C.root',
        #######'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/881A2FA2-D5E5-E711-9CF1-0CC47AD98B8E.root'
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/88958138-2ED9-E711-8665-EC0D9A0B3300.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/88C39998-DDD8-E711-86D8-001517FB20EC.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/8C72C3C9-21D7-E711-8A2B-02163E01A507.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/8CB6609D-F5DF-E711-B574-0242AC130002.root',
#        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/8E6CF263-B7E5-E711-8F97-008CFAF516CA.root',
#        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/90EFE963-11D8-E711-94D0-0025907E343C.root',
#        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/920D51B0-C1E5-E711-B179-3417EBE528B5.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/96E8305C-BBE5-E711-AFAE-0025904C66F4.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/9A76255E-C4E5-E711-BC97-001E67E71BE1.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/9C68F183-F8E4-E711-871F-24BE05BD0F81.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/9C84E3D9-EDD6-E711-AF38-02163E0118C3.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/9EDBEA7B-36D7-E711-AF85-02163E0145FE.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/30000/A05371A3-3FD8-E711-892E-0CC47A57D164.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/3CF0DD1A-03D5-E711-A785-02163E01A5B0.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/3E2C810E-E8D4-E711-8445-02163E01A50D.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/3EE9259F-C8D9-E711-A83B-A4BF01125D9E.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/4047E05A-FCD4-E711-B69E-02163E0137C1.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/42C988F7-BEDA-E711-B429-002590D9D980.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/42D749C0-27D5-E711-AB70-02163E014304.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/4405B6B8-E5DC-E711-BC76-001E677928B6.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/448D3D82-E2D9-E711-B901-008CFAC91CB8.root'
        #
        #
        #
        #
        ###--------------------------------------------------------------------------------------------------------------------------------------------- INCLUSIVE DY NLO
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/8219A333-8AE3-E611-AA70-0CC47A4C8F0C.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/8225EE18-3EE4-E611-9D47-FA163EC6E47B.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/8283DC10-5AE3-E611-A685-0CC47A546E5E.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/82D08F4A-80F1-E611-B0CC-02163E014605.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/84055A13-89F1-E611-98EC-02163E0122EE.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/84185C11-A2E3-E611-BE00-0CC47A4D765A.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/842C6C56-10E4-E611-A5B6-0025905A48F2.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/845AFA73-88F1-E611-AAA1-02163E014137.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/84AF95CE-86E4-E611-ADFB-842B2B180A9F.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/84B380A4-96E2-E611-A978-008CFA111334.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/8667484A-A0E2-E611-B471-008CFA11139C.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/86797CE5-FEE3-E611-B270-FA163E2D323D.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/86D6D486-6CE3-E611-A83E-001E673987C8.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/881D6A26-4DE4-E611-B540-FA163E702A95.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/889CDB82-19E4-E611-8EA1-FA163E7A15EC.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/88CE9104-4CE3-E611-98E9-0CC47A4D7666.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/88D00D6D-C9E3-E611-84DB-FA163EB4E50F.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/8A4B54C5-D1E7-E611-B845-B083FED42FC4.root',
        #######'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/8A8634E6-68F1-E611-BC7D-02163E019C9B.root'
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/8C03D825-87E4-E611-9990-3417EBE64B4F.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/8C29BD1C-0DE4-E611-8880-A0000420FE80.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/8E7F8A31-C4E3-E611-9755-0025905B8606.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/8E8131AA-6CF1-E611-9DC1-02163E0145B9.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/90011944-A4E3-E611-9F89-FA163E6B0874.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/901BD97C-88F1-E611-8AB6-02163E011C0C.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/90472C44-02E6-E611-AA0E-1866DAEB1FCC.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/906ECB82-C7E4-E611-A463-0025904CDDFA.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/909DB5EF-D3E3-E611-8A9F-02163E014790.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/90B81B2E-52F1-E611-833A-02163E01419B.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/90E0A071-3DE3-E611-B4CE-0025905B85D8.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/90E97CED-82F1-E611-9EA1-02163E011A0D.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/921C427E-C2E5-E611-80FF-20474791CCC4.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/92E749A1-7EE3-E611-B696-FA163EAF0CA6.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/92FE7AD0-9FE6-E611-9C0A-0CC47A1DF808.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/949D7A93-B7E3-E611-8574-90E6BA3BD76E.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/949DA4A3-AAE3-E611-977B-0025907859B4.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/949E82FD-20E4-E611-B4AB-FA163EB8639C.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/94A0F5E3-9FE6-E611-ADDA-001E674FBFC2.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/94B6116C-8AE7-E611-8B3B-842B2B760921.root' 
        ###--------------------------------------------------------------------------------------------------------------------------------------------- INCLUSIVE DY LO
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/1A8BEA4B-C5C6-E611-A82A-001E67F333BB.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/228D9B34-01C4-E611-B14F-C4346BC808B8.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/22DE75D3-27C4-E611-94AF-00237DF2A4A8.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/24239BFE-59C3-E611-A4E4-001E67F3332A.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/26649648-8CC7-E611-93B2-00266CFFBC60.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/2A2125EF-11C4-E611-98D8-00215E2EB454.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/2A70C851-FDC4-E611-8F96-008CFA11131C.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/2E1AA07C-42C5-E611-9BED-C4346BC83480.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/302A9628-9BC7-E611-AF16-001E67F33348.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/30F48B9A-68C3-E611-A945-00266CFFBE5C.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/32395D38-07C9-E611-A884-00266CFFBF38.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/348BBA75-D7C3-E611-88F0-00266CFFCC54.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/360532E5-2DC4-E611-840C-002481ACEC90.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/3ECB26B9-19C4-E611-90D6-C4346BC75558.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/4051B344-39C3-E611-B0C5-A0369F83633E.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/440F35F2-B5C3-E611-993B-001F29EACF54.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/44C5166A-23C4-E611-84C0-001E0BC1EEDE.root',
        ########'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/4A7D3294-59C6-E611-AA01-00266CFFCC54.root'
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/4CBBCFDF-F8C6-E611-A5C2-6CC2173BBD40.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/4E0A55B3-C5C3-E611-8574-00237DF2B400.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/4E81BF41-E7C3-E611-8806-00237DF2A4F0.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/50193992-44C6-E611-8B8E-6CC2173BBA30.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/525535E1-CCC3-E611-B545-001E0BC1DE40.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/585B2BBC-A9C3-E611-8DF9-002481FF6531.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/58FC5CFD-17C4-E611-8D93-00266CF91A18.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/5E58B7A4-4BC3-E611-8523-C4346BC80410.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/60CA5AE8-E0C3-E611-BD4D-00215E2EAD28.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/62A284D4-3AC5-E611-8E53-008CFA1974D8.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/62ECF90C-FDC4-E611-BA98-008CFA165F5C.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/6638E763-0FC4-E611-8661-00266CFFCB7C.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/669305F9-2DC4-E611-B161-001E0BC198E4.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/683C8BB2-B2C3-E611-B62A-001A648F1DEA.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/6A5665A0-2DC4-E611-9CAB-001A648F1E0E.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/6AB4FAEF-98C5-E611-953C-00237DF29470.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/6CCA3163-23C4-E611-B8ED-00215E2EB6A0.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/6E5577BC-1AC4-E611-9BB1-00215E2EB6A0.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/706C5E06-EAC3-E611-8D3B-008CFA0518D4.root',
        #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/720EF489-F0C3-E611-9783-00266CFFCCBC.root' 
    ))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))  



process.MyModule = cms.EDAnalyzer('GenJetAnalyzer',
)

#process.MyFilter = cms.EDFilter('jjFilter',
#)

#process.out = cms.OutputModule("PoolOutputModule",
    #fileName = cms.untracked.string("test.root"),
    #closeFileFast = cms.untracked.bool(True)
#)

process.TFileService = cms.Service("TFileService",
	#fileName = cms.string('test.root') )
	#fileName = cms.string('test_Inclusive_LO.root') )
	#fileName = cms.string('test_Inclusive_NLO.root') )
	#fileName = cms.string('test_HighMass_LO.root') )
	fileName = cms.string('test_HighMass_NLO.root') )
        #fileName = cms.string('test_Inclusive2_LO.root') )
	#fileName = cms.string('test_Inclusive2_NLO.root') )
	#fileName = cms.string('test_HighMass2_LO.root') )
	#fileName = cms.string('test_HighMass2_NLO.root') )

process.path = cms.Path(process.MyModule)
#process.path = cms.Path(process.MyFilter*process.MyModule)
