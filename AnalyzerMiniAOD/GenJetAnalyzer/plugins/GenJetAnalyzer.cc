// -*- C++ -*-
//
// Package:    AnalyzerMiniAOD/GenJetAnalyzer
// Class:      GenJetAnalyzer
// 
/**\class GenJetAnalyzer GenJetAnalyzer.cc AnalyzerMiniAOD/GenJetAnalyzer/plugins/GenJetAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Giulio Mandorli
//         Created:  Wed, 19 Jul 2017 15:14:32 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"
#include <TVector3.h>
#include <TLorentzVector.h>



#include <DataFormats/JetReco/interface/GenJet.h>
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"


#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/PatCandidates/interface/Muon.h"


// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class GenJetAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit GenJetAnalyzer(const edm::ParameterSet&);
      ~GenJetAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
           
      
      
        edm::EDGetTokenT<std::vector<reco::GenJet> > slimmedGenJetToken;
        edm::EDGetTokenT<std::vector<reco::GenParticle> > prunedGenParticlesToken;
        edm::EDGetTokenT<GenEventInfoProduct> GenEventInfoProductToken;

        edm::EDGetTokenT<std::vector<pat::Jet> > slimmedJetToken;
        edm::EDGetTokenT<std::vector<pat::PackedCandidate> > PackedCandidatesToken;
        edm::EDGetTokenT<std::vector<pat::Muon> > slimmedMuonToken;
        
        
        TTree *tree;
        edm::Service<TFileService> file;	
      
             
        
        
        int nGenMu;
        float GenMu_pt[30];
        float GenMu_eta[30];
        float GenMu_phi[30];
        float GenMu_E[30];
        float GenMu_mass[30];   
        float Mll;
        float recoMu_Mll;
        
        
        int nGenJet;
        int nrecoJet;
        int nrecoMu;
        int totalNumberRecoMu;
        int nJet_iso03;
        float GenJet_pt[30];
        float GenJet_eta[30];
        float GenJet_phi[30];
        float GenJet_E[30];
        float GenJet_mass[30];
        float GenJet_Mjj;
        float Mjj_iso03;
        float GenJet_Ht;
        float GenJet_Pt_projected_on_ll;
        
//         std::vector<float> recoMu_pt;
        float recoMu_pt[30];
        float recoMu_Iso[30];
        float recoMu_charge[30];

        
        float recoJet_Mjj;
        int weight;
        int selectionStep;
        
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
GenJetAnalyzer::GenJetAnalyzer(const edm::ParameterSet& iConfig)

{
  slimmedGenJetToken = consumes<std::vector<reco::GenJet> >(edm::InputTag("slimmedGenJets"));
  prunedGenParticlesToken = consumes<std::vector<reco::GenParticle> >(edm::InputTag("prunedGenParticles"));
  GenEventInfoProductToken = consumes<GenEventInfoProduct>(edm::InputTag("generator"));

  slimmedJetToken = consumes<std::vector<pat::Jet> >(edm::InputTag("slimmedJets"));
  PackedCandidatesToken = consumes<std::vector<pat::PackedCandidate> >(edm::InputTag("packedPFCandidates"));
    
  slimmedMuonToken = consumes<std::vector<pat::Muon> >(edm::InputTag("slimmedMuons"));
    
  
    usesResource("TFileService");
   
   
    tree=file->make<TTree>("tree","tree");

    
    tree->Branch("nGenMu", &nGenMu, "numberOfMu/I"); //"Jet_pt[10]/F"

    tree->Branch("GenMu_pt", &GenMu_pt, "GenMu_pt[30]/F"); //"Jet_pt[10]/F"
    tree->Branch("GenMu_eta", &GenMu_eta, "GenMu_eta[30]/F");
    tree->Branch("GenMu_phi", &GenMu_phi, "GenMu_phi[30]/F");
    tree->Branch("GenMu_E", &GenMu_E, "GenMu_E[30]/F");
    tree->Branch("GenMu_mass", &GenMu_mass, "GenMu_mass[30]/F");
    
    tree->Branch("GenMu_Mll", &Mll, "GenMu_Mll/F");
    tree->Branch("recoMu_Mll", &recoMu_Mll, "recoMu_Mll/F");


    tree->Branch("nGenJet", &nGenJet, "numberOfGenJet/I"); 
    tree->Branch("nGenJet_iso03", &nJet_iso03, "numberOfJet_iso03/I"); 

    tree->Branch("GenJet_pt", &GenJet_pt, "GenJet_pt[30]/F"); //"Jet_pt[10]/F"
    tree->Branch("GenJet_eta", &GenJet_eta, "GenJet_eta[30]/F");
    tree->Branch("GenJet_phi", &GenJet_phi, "GenJet_phi[30]/F");
    tree->Branch("GenJet_E", &GenJet_E, "GenJet_E[30]/F");
    tree->Branch("GenJet_mass", &GenJet_mass, "GenJet_mass[30]/F");


    tree->Branch("GenJet_Mjj", &GenJet_Mjj, "GenJet_Mjj/F");
    tree->Branch("GenJet_Mjj_iso03", &Mjj_iso03, "GenJet_Mjj_iso03/F");
    tree->Branch("weight", &weight, "weight/I");

    
    tree->Branch("GenJet_Ht", &GenJet_Ht, "GenJet_Ht/F");
    tree->Branch("GenJet_Pt_projected_on_ll", &GenJet_Pt_projected_on_ll, "GenJet_Pt_projected_on_ll/F");
    
    
    
    tree->Branch("nrecoJet", &nrecoJet, "numberOfJet/I"); 
    tree->Branch("totalNumberRecoMu", &totalNumberRecoMu, "numberOfAllMuonRecostructed/I"); 

    tree->Branch("nrecoMu", &nrecoMu, "numberOfMuonRecostructed/I"); 
//     tree->Branch("recoMu_pt", &recoMu_pt, "ptOfMuonRecostructed/F"); 
    tree->Branch("recoMu_pt", recoMu_pt, "ptOfMuonRecostructed[30]/F"); 
    tree->Branch("recoMu_Iso", recoMu_Iso, "isolationOfMuonRecostructed[30]/F"); 
    tree->Branch("recoMu_charge", recoMu_charge, "chargeOfMuonRecostructed[30]/F"); 

    
    
    tree->Branch("recoJet_Mjj", &recoJet_Mjj, "recoJet_Mjj/F");
    tree->Branch("selectionStep", &selectionStep, "selectionStep/I");

        
        
}


GenJetAnalyzer::~GenJetAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
GenJetAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   
        selectionStep = 0;
        weight = 1;
        nGenMu = 0;
        nGenJet = 0;
        nrecoJet = 0;
        nJet_iso03 = 0;
        GenJet_Mjj = 0;
        Mjj_iso03 = 0;
        int MuIdx=0;
        
        recoMu_Mll=0;
        totalNumberRecoMu = 0;
        
        GenJet_Ht=0;
        GenJet_Pt_projected_on_ll=0;
        
        
//         while(recoMu_pt.size() > 0) recoMu_pt.clear();
        
        
        
        for (int n=0; n<30;++n) {
            GenJet_pt[n]=0;
            GenJet_eta[n]=0;
            GenJet_phi[n]=0;
            GenJet_E[n]=0;
            GenJet_mass[n]=0;
            
            recoMu_pt[n]=0;
            recoMu_Iso[n]=-0.1;
            recoMu_charge[n]=0;

            GenMu_pt[n]=0;
            GenMu_eta[n]=0;
            GenMu_phi[n]=0;
            GenMu_E[n]=0;
            GenMu_mass[n]=0;  
        }



        Handle<std::vector<reco::GenJet>> genJetsCollection;
        iEvent.getByToken(slimmedGenJetToken, genJetsCollection);
        std::vector<reco::GenJet>  jets = *genJetsCollection.product();
        

        
        Handle<std::vector<reco::GenParticle>> genParticelesCollection;
        iEvent.getByToken(prunedGenParticlesToken, genParticelesCollection);
        auto  genParticles = *genParticelesCollection.product();
        
        
        Handle<GenEventInfoProduct> EventInf;
        iEvent.getByToken(GenEventInfoProductToken, EventInf);
        auto  genInfo = *EventInf.product();
        

        
        
        
        
        
        
        double genWeight = EventInf->weight();
        if (genWeight < 0) weight = -1;
        
        
        
        
        
        
        
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////GEN OBJECT/////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        std::vector<TLorentzVector> mu_vector;
        std::vector<TLorentzVector> lep_vector;
        for(std::vector<reco::GenParticle>::const_iterator pit = genParticles.begin() ; pit != genParticles.end() && MuIdx < 30 ; ++pit) {

            if (((abs(pit->pdgId()) == 11) || (abs(pit->pdgId()) == 13) || (abs(pit->pdgId()) == 15)) && pit->isHardProcess()) {
//             if ( (abs(pit->pdgId()) == 13) && pit->isHardProcess()) {
                
                TLorentzVector tmpVector;
                tmpVector.SetPtEtaPhiM(pit->p4().pt(), pit->p4().Eta(), pit->p4().Phi(), pit->p4().M());
                lep_vector.push_back(tmpVector);
                
                if (abs(pit->pdgId()) == 13) {
                    GenMu_pt[MuIdx] = pit->p4().pt();
                    GenMu_eta[MuIdx] = pit->p4().Eta();
                    GenMu_phi[MuIdx] = pit->p4().Phi();
                    GenMu_E[MuIdx] = pit->p4().E();
                    GenMu_mass[MuIdx] = pit->p4().M(); 
                    ++MuIdx;

                    mu_vector.push_back(tmpVector);
                }
            }
        }
        
        
        
        nGenMu = mu_vector.size();
        
        
        std::vector<TLorentzVector> jets_noLep03; 
        std::vector<TLorentzVector> jets_vector;

        nGenJet = jets.size();
        int jet_iso03_idx=0;
        int jet_idx = 0;
        int n = 0;
        if (nGenMu > 1 ) {
            Mll = (mu_vector[0] + mu_vector[1]).M();
            for(std::vector<reco::GenJet>::const_iterator jit = jets.begin() ; jit != jets.end() && jets_vector.size() < 30 && jet_iso03_idx < 30 ; ++jit) {

            if ( jit->pt()>5 && abs(jit->eta())<5) {


                if (jit->pt() < -1000) std::cout  << std::endl << n << " \t " << jit->pt() << std::endl;
        
                TLorentzVector tmpVector;
                tmpVector.SetPtEtaPhiM(jit->pt(),jit->eta(),jit->phi(),jit->mass());
                
                float theta1 = mu_vector[0].DeltaR(tmpVector);
                float theta2 = mu_vector[1].DeltaR(tmpVector);
                if (theta1 > 0.3 && theta2 > 0.3) {                
                    if(1) {
            
                            GenJet_pt[jet_idx] = jit->pt();
                            GenJet_eta[jet_idx] = jit->eta();
                            GenJet_phi[jet_idx] = jit->phi();
                            GenJet_E[jet_idx] = jit->energy();
                            GenJet_mass[jet_idx] = jit->mass(); 
                            jet_idx++;
                            jets_vector.push_back(tmpVector);
                            GenJet_Ht = GenJet_Ht + jit->pt();
                    }
                }
                
                
                
//                 -------------------------------------------------------------CODE FOR ISO03--------------------------------------------------------------------------------------
//                     float theta1 = mu_vector[0].DeltaR(tmpVector);
//                     float theta2 = mu_vector[1].DeltaR(tmpVector);
//                     if (theta1 > 0.3 && theta2 > 0.3) {
//                         jets_noLep03.push_back(tmpVector);
//                         Jet_pt[jet_iso03_idx] = jit->pt();
//                         Jet_eta[jet_iso03_idx] = jit->eta();
//                         Jet_phi[jet_iso03_idx] = jit->phi();
//                         Jet_E[jet_iso03_idx] = jit->energy();
//                         Jet_mass[jet_iso03_idx] = jit->mass();   
//                         ++jet_iso03_idx;
//                     }
// 
//                     if (jets_noLep03.size() == 2 ) {
//                         Mjj_iso03 = (jets_noLep03[0] + jets_noLep03[1]).M();
//                     }
//                 -------------------------------------------------------------CODE FOR ISO03--------------------------------------------------------------------------------------

                
                
                
                
                }
            ++n;            
                
            }         
        } //end nGenMu > 1 condition
        
        nJet_iso03 = jets_noLep03.size();
        nJet_iso03 = jets_vector.size();
    
        
        if (jets_vector.size()>1) {
         
            GenJet_Mjj = (jets_vector[0] + jets_vector[1]).M();
        }
          
          
          
                
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////END GEN OBJECT/////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  
          
          
          
          
          
          
          
        nrecoMu = 0;
        nrecoJet = 0;
        recoJet_Mjj = 0;
          
          
          
        Handle<std::vector<pat::Jet>> jetsCollection;
        iEvent.getByToken(slimmedJetToken, jetsCollection);
        std::vector<pat::Jet>  patJets = *jetsCollection.product();
        

        
        Handle<std::vector<pat::PackedCandidate>> PackedCandidatesCollection;
        iEvent.getByToken(PackedCandidatesToken, PackedCandidatesCollection);
        auto  packedCandidate = *PackedCandidatesCollection.product();
          

        Handle<std::vector<pat::Muon>> patMuonsCollection;
        iEvent.getByToken(slimmedMuonToken, patMuonsCollection);
        std::vector<pat::Muon>  patMuons= *patMuonsCollection.product();  
        
        
        
        
        
//         std::vector<TLorentzVector> mu_reco;
//         int firstMuonCharge = 0;
//         for(std::vector<pat::PackedCandidate>::const_iterator pit = packedCandidate.begin() ; pit != packedCandidate.end() ; ++pit) {
//             if (abs(pit->pdgId()) == 13 /*/&& pit->muonID() && pit->isPFMuon() && pit->isolationR03()/*/) { 
//                 totalNumberRecoMu++;
//                 recoMu_pt[n] = pit->p4().pt();
//                 if (mu_reco.size() == 2) {nrecoMu++; continue;}
//                 if (mu_reco.size() == 1 && firstMuonCharge*pit->charge() > 0 ) {nrecoMu++; continue;}
//                 if (mu_reco.size() < 2) {
//                     firstMuonCharge = pit->charge();
//                     TLorentzVector tmpVector;
//                     tmpVector.SetPtEtaPhiM(pit->p4().pt(), pit->p4().Eta(), pit->p4().Phi(), pit->p4().M());
//                     mu_reco.push_back(tmpVector);
//                 }
//             }
//         }
        
        
        
        
//         totalNumberRecoMu = patMuons.size();

        std::vector<TLorentzVector> mu_reco;
        int firstMuonCharge = 0;
        int mu_idx = 0;
        for(std::vector<pat::Muon>::const_iterator pit = patMuons.begin() ; pit != patMuons.end() ; ++pit) {
            
            if ( /*/ pit->muonID("TMOneStationTight") && pit->isPFMuon() &&/*/ pit->p4().pt() > 3 && abs(pit->p4().Eta()) < 2.4 && pit->track().isNonnull()) {     // Non sono riuscito a mettere i limiti su dxy < 0.5 e dz < 1.0         https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/Heppy/python/analyzers/objects/LeptonAnalyzer.py#L174
                if( pit->isPFMuon() &&  (pit->isGlobalMuon() || pit->isTrackerMuon())) { // this selection is muonID("POG_ID_Loose")    https://github.com/cms-sw/cmssw/blob/master/DataFormats/MuonReco/src/MuonSelectors.cc#L871
                    
                    recoMu_charge[mu_idx] = pit->charge();
                    recoMu_pt[mu_idx] = pit->p4().pt();
                    recoMu_Iso[mu_idx] = (pit->pfIsolationR04().sumChargedHadronPt + std::max( pit->pfIsolationR04().sumNeutralHadronEt +  pit->pfIsolationR04().sumPhotonEt -  pit->pfIsolationR04().sumPUPt/2, (float) 0.0))/pit->p4().pt();
    //                 if (recoMu_Iso[n]<0.25) {
                        totalNumberRecoMu++;
                        if (mu_reco.size() == 2)  continue;
                        if (mu_reco.size() == 1 && firstMuonCharge*pit->charge() > 0 )  continue;
                        if (mu_reco.size() < 2) {
                            firstMuonCharge = pit->charge();
                            TLorentzVector tmpVector;
                            tmpVector.SetPtEtaPhiM(pit->p4().pt(), pit->p4().Eta(), pit->p4().Phi(), pit->p4().M());
                            mu_reco.push_back(tmpVector);
                    }
                mu_idx++;
                }
            }
        }
        

        
        
        
        
        
        std::vector<TLorentzVector> jet_reco;
        for(std::vector<pat::Jet>::const_iterator jit = patJets.begin() ; jit != patJets.end() ; ++jit) {
            
            
            TLorentzVector tmpVector;
            tmpVector.SetPtEtaPhiM(jit->p4().pt(), jit->p4().Eta(), jit->p4().Phi(), jit->p4().M());
            
            float theta1 = 100;
            float theta2 = 100;
            
            if(mu_reco.size() > 0)  theta1 = mu_reco[0].DeltaR(tmpVector);
            if(mu_reco.size() > 1)  theta2 = mu_reco[1].DeltaR(tmpVector);
            if (theta1 > 0.3 && theta2 > 0.3) {         
                float eta = abs(jit->p4().Eta());
//                 if(jit->jetID()) {
                if((eta<3.0 && ((jit->chargedMultiplicity() + jit->neutralMultiplicity()>1 && jit->neutralEmEnergyFraction() <0.99 && jit->neutralHadronEnergyFraction()<0.99) && (eta>2.4 || (jit->chargedEmEnergyFraction() <0.99 && jit->chargedHadronEnergyFraction() >0 && jit->chargedHadronMultiplicity()>0)))) || (eta>3.0 && (jit->neutralEmEnergyFraction() <0.90 && jit->neutralMultiplicity()>10)))    {    //this selection is jet.jetID('POG_PFID_Loose')  https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/Heppy/python/physicsobjects/Jet.py#L98
//                                Selection on puJetID() is still missing         https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/Heppy/python/physicsobjects/Jet.py#L143

                    jet_reco.push_back(tmpVector);
                }
            }
        }    
        
        
        
        if(mu_reco.size() > 1) recoMu_Mll = (mu_reco[0] + mu_reco[1]).M();
        
        
        
        nrecoJet = jet_reco.size();
        nrecoMu = mu_reco.size();
        
        if(jet_reco.size() > 1) {
            selectionStep = 1; 
            
            
            TLorentzVector qq_p4 =  jet_reco[0] + jet_reco[1];
            recoJet_Mjj = qq_p4.M();

            
            if(mu_reco.size() == 2) {
                selectionStep = 2;
                
                TLorentzVector Hll_p4 =  mu_reco[0] + mu_reco[1];
                float Hll_p4_mass = Hll_p4.M();
                float Hll_ystar = Hll_p4.Rapidity() - (jet_reco[0].Rapidity() + jet_reco[1].Rapidity()) ;
                float Hll_zstar = TMath::Abs( Hll_ystar/ (jet_reco[0].Rapidity()-jet_reco[1].Rapidity() )) ;
                

                
//                 if (Hll_p4_mass > 110) {
//                      selectionStep = 3;
                    
                
                    if (Hll_p4_mass < 145) {
                        selectionStep = 4;
            
                        
//                         if (recoJet_Mjj > 200) {
//                             selectionStep = 5;
                                                                                       
                        if (recoMu_Iso[0] < 0.25 && recoMu_Iso[1] < 0.25) {
                            selectionStep = 5;
                                                                    
                                                                    

                            if (jet_reco[0].Pt() > 35) {
                                selectionStep = 6;
                            
                                if (jet_reco[1].Pt() > 25) {                   
                                    selectionStep = 7;
                                
                                
                                    if (mu_reco[0].Pt() > 30) {
                                        selectionStep = 8;
                                    
                                        if (mu_reco[1].Pt() > 10) {                   
                                            selectionStep = 9;                            
                            
                                        
                                            if (abs(mu_reco[0].Eta()) < 2.4) {
                                                selectionStep = 10;
                                            
                                                if (abs(mu_reco[1].Eta()) < 2.4) {                   
                                                    selectionStep = 11;                     
                            
                                                    if (1) { //selezione sul bTagging
                                                        selectionStep = 12;
                                                        
                                                        if ( abs(jet_reco[0].Eta() - jet_reco[1].Eta()) < 2.5) {
                                                            selectionStep = 13;
                                                            
                                                            if (Hll_zstar < 2.5) {
                                                                selectionStep = 14;
                                                                

                                                                
                                                                }
                                                    
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                        
                            }
//                         }
                    }
//                 }
            }
        }
        
        
        
        
              
              
              
          
                               
          
        tree->Fill();
        
        
}


// ------------ method called once each job just before starting event loop  ------------
void 
GenJetAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenJetAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenJetAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenJetAnalyzer);
