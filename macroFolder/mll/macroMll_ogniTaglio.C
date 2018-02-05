#include <stdio.h>
#include <iostream>


#include "TTree.h"
#include <TVector3.h>
#include <TLorentzVector.h>

#include <ctype.h>
#include <iomanip>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cstdlib>
#include "TFile.h"
#include "TH1.h"
#include "TH1F.h"
#include "TH2.h"
#include "TTree.h"
#include "TChain.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm> 
#include <TROOT.h>
#include <TString.h>
#include <TStyle.h>
#include <TSystem.h>
#include <TCanvas.h>
#include <TMarker.h>
#include <THStack.h>
#include <TLegend.h>
#include <TLatex.h>
#include <TCut.h>
#include <TGraph.h>
#include <TGraphErrors.h>
#include <TLorentzVector.h>
#include <TMath.h>
#include <TF1.h>
#include <TProfile.h>
#include "math.h"



void Write (std::ofstream out_efficiency, TH2F * histo) {
    
    for(int n=0; histo->GetNbinsX(); ++n) 
    out_efficiency << "prova";


    
}






void SetStyle_and_Save (TCanvas * canv, TH1 * histo, std::string xTitle, std::string name, std::string yTitle="Entries") {
    
    histo->SetLineWidth(3);
    histo->SetLineColor(kBlue);

    histo->GetYaxis()->SetTitle(yTitle.c_str());
    histo->GetXaxis()->SetTitle(xTitle.c_str());

    
//     float axisTitleSize=0.05;
//     histo->GetYaxis()->SetTitleSize(axisTitleSize);
//     histo->GetXaxis()->SetTitleSize(axisTitleSize);
//     
//     float axisTitleOffset=0.05;
//     histo->GetYaxis()->SetTitleOffset(axisTitleOffset);
//     histo->GetXaxis()->SetTitleOffset(axisTitleOffset);
//     
//     
//     float axisLabelSize=0.05;
//     histo->GetYaxis()->SetLabelSize(axisLabelSize);
//     histo->GetXaxis()->SetLabelSize(axisLabelSize);
//     
//     float axisLabelOffset=0.05;
//     histo->GetYaxis()->SetLabelOffset(axisLabelOffset);
//     histo->GetXaxis()->SetLabelOffset(axisLabelOffset);
    
    
    
    
    canv->cd();
    
    histo->Draw();
    canv->Print(("figure/"+name+".png").c_str());
}

std::string makeString(float x, int n) {
    
    stringstream ss_x;
    ss_x << std::setprecision(n) << x;
    return  ss_x.str();
    
}


void DrawSame_and_Save(TCanvas * canv, TH1 * histo1, TH1 * histo2,TLegend * leg,std::string name, std::string nameSample) {
    canv->cd(1);
    gStyle->SetOptStat(0000);
    gPad->SetLogy();   
    
    histo2->SetLineColor(kRed);
    histo1->GetYaxis()->SetTitle("Entries");
    histo1->Draw();
    histo2->Draw("same");
    leg->Draw();
    
    double error1 = 0;
    double error2 = 0;

    float integral1 = histo1->IntegralAndError(0, histo1->GetXaxis()->GetNbins()+1, error1);
    float integral2 = histo2->IntegralAndError(0, histo2->GetXaxis()->GetNbins()+1, error2);
    float error = sqrt(error1*error1/integral1/integral1 + error2*error2/integral2/integral2); 
    double ratio = integral2/integral1;
    error = error * ratio;
                
    string ratio_str = makeString(ratio, 3);
    string error_str = makeString(error, 2);
    
    string integral1_str = makeString(integral1, 4);
    string integral2_str = makeString(integral2, 4);
    
    string integralErr1_str = makeString(error1, 3);
    string integralErr2_str = makeString(error2, 3);
    
    
    
    
    double error1_highRegion = 0;
    double error2_highRegion = 0;

    float integral1_highRegion = histo1->IntegralAndError(histo1->GetXaxis()->FindBin(110), histo1->GetXaxis()->FindBin(145), error1_highRegion);
    float integral2_highRegion = histo2->IntegralAndError(histo2->GetXaxis()->FindBin(110), histo2->GetXaxis()->FindBin(145), error2_highRegion);
    float error_highRegion = sqrt(error1_highRegion*error1_highRegion/integral1_highRegion/integral1_highRegion + error2_highRegion*error2_highRegion/integral2_highRegion/integral2_highRegion); 
    double ratio_highRegion = integral2_highRegion/integral1_highRegion;

                
    stringstream ss_ratio_highRegion;
    ss_ratio_highRegion << std::setprecision(3) << ratio_highRegion;
    string ratio_str_highRegion = ss_ratio_highRegion.str();
    
    stringstream ss_error_highRegion;
    ss_error_highRegion << std::setprecision(2) << error_highRegion;
    string error_str_highRegion = ss_error_highRegion.str();
    
    
    
    
    float yt2 = 0.15;
    float xt2 = 0.25;
    TLatex * t1 = new TLatex(xt2,yt2+0.05 ,("NLO/LO="+ratio_str+" +- "+error_str).c_str());
    t1->SetNDC();
    t1->SetTextAlign(22);
    t1->SetTextSize(0.04);
    t1->Draw();
    
    
    TLatex * t2 = new TLatex(xt2+0.07 ,yt2 ,("NLO/LO="+ratio_str_highRegion+" +- "+error_str_highRegion+" in 110<Mll<145").c_str());
    t2->SetNDC();
    t2->SetTextAlign(22);
    t2->SetTextSize(0.04);
    std::string histoName = histo2->GetName();
    if(histoName.find("hMll_NLO")!=std::string::npos) t2->Draw();
    
    
    
    TLatex * t3 = new TLatex(xt2+0.5,yt2 ,("LO  ="+integral1_str + " +- " + integralErr1_str+" %").c_str());
    t3->SetNDC();
    t3->SetTextAlign(22);
    t3->SetTextSize(0.04);
    t3->Draw();
    
    
    TLatex * t4 = new TLatex(xt2+0.5,yt2+0.05 ,("NLO ="+integral2_str + " +- " + integralErr2_str+" %").c_str());
    t4->SetNDC();
    t4->SetTextAlign(22);
    t4->SetTextSize(0.04);
    t4->Draw();
    
    
    
    canv->cd(2);
    gStyle->SetOptStat(0000);
    gPad->SetGrid();  
 
    TH1F * hRatio = (TH1F*) histo2->Clone(name.c_str());
     
    hRatio->GetYaxis()->SetTitle("NLO/LO");
    hRatio->GetYaxis()->SetTitleSize(0.05);
    hRatio->GetYaxis()->SetTitleOffset(1.);
    
    hRatio->GetYaxis()->SetRangeUser(0.5, 1.5);
    hRatio->Divide(histo1);
    hRatio->Draw();    
    
    
    
    
    canv->Print(("figure/"+name+"_"+nameSample+".png").c_str());
    
}




// main() {
void macroMll_ogniTaglio () {


        std::cout << "I can see here" << std::endl;
    

//         TFile * f_NLO = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_Inclusive_NLO.root");
//         TFile * f_LO  = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_Inclusive_LO.root");
//         TFile * f_NLO = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_HighMass_NLO.root");
//         TFile * f_LO  = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_HighMass_LO.root");
        
 
        TFile * f_NLO = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_HighMass_NLO_Final.root");
        TFile * f_LO  = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_HighMass_LO_Final.root");
        
        
        
//         TFile * f_NLO = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_InclusiveSum_NLO.root");
//         TFile * f_LO  = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_InclusiveSum_LO.root");

        
//         TFile * f_NLO = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_HighMassSum_NLO.root");
//         TFile * f_LO  = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_HighMassSum_LO.root");
        
        
        f_NLO->cd("MyModule");
        f_LO->cd("MyModule");

        
        
        
        TTree * tree_NLO = (TTree*) f_NLO->Get("MyModule/tree");
        TTree * tree_LO  = (TTree*) f_LO->Get("MyModule/tree");

        
        int nentries_NLO = tree_NLO->GetEntries();
        int nentries_LO  = tree_LO->GetEntries();
        

        std::string nameSample = "Inclusive";
        nameSample = "highMass";

       
        TCanvas * canv = new TCanvas ("c", "c", 800,1000); 
        canv->Divide(1,2);
        
        float mll_max = 0;
        float mll_min = 0;
        if(nameSample.find("Inclusive")!=std::string::npos) {
            mll_max = 150;
            mll_min = 60;
            
        }
        if(nameSample.find("highMass")!=std::string::npos) {
            mll_max = 150;
            mll_min = 90;
            
        }
        std::vector<TH1F*> hVEC_Mll_NLO;
        std::vector<TH1F*> hVEC_Mll_LO;
        
        
        std::vector<TH1F*> hVEC_genMqq_NLO;
        std::vector<TH1F*> hVEC_genMqq_LO;     
        std::vector<TH1F*> hVEC_recoMqq_NLO;
        std::vector<TH1F*> hVEC_recoMqq_LO; 
        
        std::vector<TH1F*> hVEC_nrecoJet_NLO; 
        std::vector<TH1F*> hVEC_nrecoJet_LO; 

        std::vector<TH1F*> hVEC_genJet_Ht_NLO; 
        std::vector<TH1F*> hVEC_genJet_Ht_LO; 

        float ptMin = 0;
        float ptMax = 120;
        std::vector<TH1F*> hVEC_pt1q_NLO;
        std::vector<TH1F*> hVEC_pt1q_LO; 
        std::vector<TH1F*> hVEC_pt2q_NLO;
        std::vector<TH1F*> hVEC_pt2q_LO;
        std::vector<TH1F*> hVECqqDeltaEta_NLO;
        std::vector<TH1F*> hVECqqDeltaEta_LO;
        
        
        std::vector<TH1F*> hVECrecoPt_q_NLO;
        std::vector<TH1F*> hVECrecoPt_q_LO;
        std::vector<TH1F*> hVECrecoPt1_q_NLO;
        std::vector<TH1F*> hVECrecoPt1_q_LO;
        std::vector<TH1F*> hVECrecoPt2_q_NLO;
        std::vector<TH1F*> hVECrecoPt2_q_LO;

        
        
        
//         std::vector<std::string> cutNames = {"no cut", "#jet > 1", "#mu = 2", "mll > 110", "mll < 145", "Mjj > 200", "pT_1q >35", "pT_2q >25", "pT_1mu >30", "pT_2mu >10", "|eta_1mu| <2.4", "|eta_2mu| <2.4", "   ", "|eta_qq| <2.5", "z*<2.5", "Mqq > 200"};
//         std::vector<std::string> cutNames = {"no cut", "#jet > 1", "#mu = 2", "", "mll < 145", "", "pT_1q >35", "pT_2q >25", "pT_1mu >30", "pT_2mu >10", "|eta_1mu| <2.4", "|eta_2mu| <2.4", "   ", "|eta_qq| <2.5", "Mqq > 200"};
        std::vector<std::string> cutNames = {"no cut", "#jet > 1", "#mu = 2", "mll > 110", "mll < 145", "muon isolation", "pT_1q >35", "pT_2q >25", "pT_1mu >30", "pT_2mu >10", "|eta_1mu| <2.4", "|eta_2mu| <2.4", "   ", "z*<2.5", "|eta_qq| >2.5", "preselection"};
        
        
        int nCut = 16;
        for(int n = 0; n < nCut; n++) {
            
            stringstream ss;
            ss << n;
            string n_str = ss.str();

            if (n < 10) n_str = "0"+n_str;

            TH1F * hMll_NLO = new TH1F (("hMll_NLO"+n_str).c_str(), (cutNames[n]+";Mll [GeV];").c_str(), 35, mll_min, mll_max); 
            TH1F * hMll_LO = new TH1F (("hMll_LO"+n_str).c_str(), (cutNames[n]+";Mll [GeV];").c_str(), 35, mll_min, mll_max); 
            hMll_NLO->Sumw2();
            hMll_LO->Sumw2();
            
            
            TH1F * hgenMqq_NLO = new TH1F (("hgenMqq_NLO"+n_str).c_str(), (cutNames[n]+";gen Mqq [GeV];").c_str(), 35, 0, 400); 
            TH1F * hgenMqq_LO = new TH1F (("hgenMqq_LO"+n_str).c_str(), (cutNames[n]+";gen Mqq [GeV];").c_str(), 35, 0, 400); 
            hgenMqq_NLO->Sumw2();
            hgenMqq_LO->Sumw2();
            
            
            TH1F * hrecoMqq_NLO = new TH1F (("hrecoMqq_NLO"+n_str).c_str(), (cutNames[n]+";reco Mqq [GeV];").c_str(), 35, 0, 400); 
            TH1F * hrecoMqq_LO = new TH1F (("hrecoMqq_LO"+n_str).c_str(), (cutNames[n]+";reco Mqq [GeV];").c_str(), 35, 0, 400); 
            hrecoMqq_NLO->Sumw2();
            hrecoMqq_LO->Sumw2();
            

            TH1F * hpt1q_NLO = new TH1F (("hpt1q_NLO"+n_str).c_str(), (cutNames[n]+";pt(1q) [GeV];").c_str(), 35, ptMin, ptMax); 
            TH1F * hpt1q_LO  = new TH1F (("hpt1q_LO"+n_str).c_str(), (cutNames[n]+";pt(1q) [GeV];").c_str(), 35, ptMin, ptMax); 
            hpt1q_NLO->Sumw2();
            hpt1q_LO->Sumw2(); 
            
            
            TH1F * hpt2q_NLO = new TH1F (("hpt2q_NLO"+n_str).c_str(), (cutNames[n]+";pt(2q) [GeV];").c_str(), 35, ptMin, ptMax); 
            TH1F * hpt2q_LO  = new TH1F (("hpt2q_LO"+n_str).c_str(), (cutNames[n]+";pt(2q) [GeV];").c_str(), 35, ptMin, ptMax); 
            hpt2q_NLO->Sumw2();
            hpt2q_LO->Sumw2();

            
            
            TH1F * hnrecoJet_NLO = new TH1F (("hnrecoJet_NLO"+n_str).c_str(), (cutNames[n]+";# reco jets;").c_str(), 12, 0, 12); 
            TH1F * hnrecoJet_LO  = new TH1F (("hnrecoJet_LO"+n_str).c_str(), (cutNames[n]+";# reco jets;").c_str(), 12, 0, 12); 
            hnrecoJet_NLO->Sumw2();
            hnrecoJet_LO->Sumw2();
            
            
            TH1F * hgenJet_Ht_NLO = new TH1F (("hgenJet_Ht_NLO"+n_str).c_str(), (cutNames[n]+";gen H_T [GeV];").c_str(), 35, ptMin, ptMax); 
            TH1F * hgenJet_Ht_LO  = new TH1F (("hgenJet_Ht_LO"+n_str).c_str(), (cutNames[n]+";gen H_T [GeV];").c_str(), 35, ptMin, ptMax); 
            hgenJet_Ht_NLO->Sumw2();
            hgenJet_Ht_LO->Sumw2();
            
            
            
            TH1F * hqqDeltaEta_NLO = new TH1F (("hqqDeltaEta_NLO"+n_str).c_str(), (cutNames[n]+";#Delta #eta (qq);").c_str(), 30, 0, 8); 
            TH1F * hqqDeltaEta_LO  = new TH1F (("hqqDeltaEta_LO"+n_str).c_str(), (cutNames[n]+";#Delta #eta (qq);").c_str(), 30, 0, 8); 
            hqqDeltaEta_NLO->Sumw2();
            hqqDeltaEta_LO->Sumw2();
            
            
            
            TH1F * hrecoPt_q_NLO = new TH1F (("hrecoPt_q_NLO"+n_str).c_str(), (cutNames[n]+";reco all pt [GeV];").c_str(), 35, ptMin, ptMax); 
            TH1F * hrecoPt_q_LO  = new TH1F (("hrecoPt_q_LO"+n_str).c_str(), (cutNames[n]+";reco all pt [GeV];").c_str(), 35, ptMin, ptMax); 
            hrecoPt_q_NLO->Sumw2();
            hrecoPt_q_LO->Sumw2(); 
            
            
            TH1F * hrecoPt1_q_NLO = new TH1F (("hrecoPt1_q_NLO"+n_str).c_str(), (cutNames[n]+";reco pt(1q) [GeV];").c_str(), 35, ptMin, ptMax); 
            TH1F * hrecoPt1_q_LO  = new TH1F (("hrecoPt1_q_LO"+n_str).c_str(), (cutNames[n]+";reco pt(1q) [GeV];").c_str(), 35, ptMin, ptMax); 
            hrecoPt1_q_NLO->Sumw2();
            hrecoPt1_q_LO->Sumw2(); 
            
            
            TH1F * hrecoPt2_q_NLO = new TH1F (("hrecoPt2_q_NLO"+n_str).c_str(), (cutNames[n]+";reco pt(2q) [GeV];").c_str(), 35, ptMin, ptMax); 
            TH1F * hrecoPt2_q_LO  = new TH1F (("hrecoPt2_q_LO"+n_str).c_str(), (cutNames[n]+";reco pt(2q) [GeV];").c_str(), 35, ptMin, ptMax); 
            hrecoPt2_q_NLO->Sumw2();
            hrecoPt2_q_LO->Sumw2(); 
            
            
            
            
            
            
            
            
            hVEC_Mll_NLO.push_back(hMll_NLO);
            hVEC_Mll_LO.push_back(hMll_LO);
            
            hVEC_genMqq_NLO.push_back(hgenMqq_NLO);
            hVEC_genMqq_LO.push_back(hgenMqq_LO);
            hVEC_recoMqq_NLO.push_back(hrecoMqq_NLO);
            hVEC_recoMqq_LO.push_back(hrecoMqq_LO);
            
            
            hVEC_pt1q_NLO.push_back(hpt1q_NLO);
            hVEC_pt1q_LO.push_back(hpt1q_LO);
            hVEC_pt2q_NLO.push_back(hpt2q_NLO);
            hVEC_pt2q_LO.push_back(hpt2q_LO);
            hVECqqDeltaEta_NLO.push_back(hqqDeltaEta_NLO);
            hVECqqDeltaEta_LO.push_back(hqqDeltaEta_LO);
            
            
            hVEC_nrecoJet_NLO.push_back(hnrecoJet_NLO);
            hVEC_nrecoJet_LO.push_back(hnrecoJet_LO);
            hVEC_genJet_Ht_NLO.push_back(hgenJet_Ht_NLO);
            hVEC_genJet_Ht_LO.push_back(hgenJet_Ht_LO);
        
            
            hVECrecoPt_q_NLO.push_back(hrecoPt_q_NLO);
            hVECrecoPt_q_LO.push_back(hrecoPt_q_LO);
            hVECrecoPt1_q_NLO.push_back(hrecoPt1_q_NLO);
            hVECrecoPt1_q_LO.push_back(hrecoPt1_q_LO);
            hVECrecoPt2_q_NLO.push_back(hrecoPt2_q_NLO);
            hVECrecoPt2_q_LO.push_back(hrecoPt2_q_LO);
            
            
            
        }
        
        
        
        
        
        
        
        
        float GenMll_NLO=0;
        float GenMll_LO=0;    
        float recoMu_Mll_NLO=0;
        float recoMu_Mll_LO=0;
        int weight_NLO = 0;
        int weight_LO = 0;
        float Mjj_NLO = 0;
        float Mjj_LO = 0;
        float recoJet_Mjj_NLO = 0;
        float recoJet_Mjj_LO = 0;
        
        float recoPt_q_NLO[30]={};
        float recoPt1_q_NLO = 0;
        float recoPt2_q_NLO = 0;
        
        float recoPt_q_LO[30]={};
        float recoPt1_q_LO = 0;
        float recoPt2_q_LO = 0;
        
        
        float pt_q_NLO[30]={};
        float pt_q_LO[30]={};

        int nrecoJet_NLO = 0;
        int nrecoJet_LO = 0;
        float GenJet_Ht_NLO = 0;
        float GenJet_Ht_LO = 0;
        
        
        float qqDeltaEta_NLO=0;
        float qqDeltaEta_LO=0;
        
        
        int selectionStep_NLO=0;
        int selectionStep_LO=0;

                        
        tree_NLO->SetBranchAddress("GenMu_Mll", &GenMll_NLO);
        tree_NLO->SetBranchAddress("recoMu_Mll", &recoMu_Mll_NLO);
        tree_NLO->SetBranchAddress("weight", &weight_NLO);
        tree_NLO->SetBranchAddress("GenJet_Mjj", &Mjj_NLO);
        tree_NLO->SetBranchAddress("GenJet_pt", &pt_q_NLO);
        tree_NLO->SetBranchAddress("recoJet_pt", &recoPt_q_NLO);
        tree_NLO->SetBranchAddress("recoJet_pt1", &recoPt1_q_NLO);
        tree_NLO->SetBranchAddress("recoJet_pt2", &recoPt2_q_NLO);
        tree_NLO->SetBranchAddress("qqDeltaEta", &qqDeltaEta_NLO);
        tree_NLO->SetBranchAddress("recoJet_Mjj", &recoJet_Mjj_NLO);
        tree_NLO->SetBranchAddress("selectionStep", &selectionStep_NLO);
        tree_NLO->SetBranchAddress("nrecoJet", &nrecoJet_NLO);
        tree_NLO->SetBranchAddress("GenJet_Ht", &GenJet_Ht_NLO);
        
        
        tree_LO->SetBranchAddress("GenMu_Mll", &GenMll_LO);
        tree_LO->SetBranchAddress("recoMu_Mll", &recoMu_Mll_LO);
        tree_LO->SetBranchAddress("weight", &weight_LO);
        tree_LO->SetBranchAddress("GenJet_Mjj", &Mjj_LO);
        tree_LO->SetBranchAddress("GenJet_pt", &pt_q_LO);
        tree_LO->SetBranchAddress("recoJet_pt", &recoPt_q_LO);
        tree_LO->SetBranchAddress("recoJet_pt1", &recoPt1_q_LO);
        tree_LO->SetBranchAddress("recoJet_pt2", &recoPt2_q_LO);
        tree_LO->SetBranchAddress("qqDeltaEta", &qqDeltaEta_LO);
        tree_LO->SetBranchAddress("recoJet_Mjj", &recoJet_Mjj_LO);
        tree_LO->SetBranchAddress("selectionStep", &selectionStep_LO);
        tree_LO->SetBranchAddress("nrecoJet", &nrecoJet_LO);
        tree_LO->SetBranchAddress("GenJet_Ht", &GenJet_Ht_LO);


        int total = 0;
        float w=1;

        for (int entry=0; entry<nentries_NLO;++entry){

            tree_NLO->GetEntry(entry);
              
/*            if (weight_NLO>-0.5) w = 1.;
            else w = -1; */         
            w = weight_NLO;

            if (abs(weight_NLO) > 2) continue;  
            
//              if (recoMu_Mll_NLO < 55) continue;
//             if ((recoMu_Mll_NLO < 75) || (recoMu_Mll_NLO > 105)) continue;
//             if ((GenMll_NLO < 75) || (GenMll_NLO > 105)) continue;

            for(int n = 0; n < nCut-1; n++) {
                if (selectionStep_NLO >= n) {
                    if (selectionStep_NLO >= 3 && recoMu_Mll_NLO<110) continue;
                    hVEC_Mll_NLO[n]->Fill(recoMu_Mll_NLO, w);
//                     hVEC_Mll_NLO[n]->Fill(GenMll_NLO, w);
                    hVEC_genMqq_NLO[n]->Fill(Mjj_NLO, w);
                    hVEC_recoMqq_NLO[n]->Fill(recoJet_Mjj_NLO, w);
                    hVEC_pt1q_NLO[n]->Fill(pt_q_NLO[0], w);
                    hVEC_pt2q_NLO[n]->Fill(pt_q_NLO[1], w);
                    hVECqqDeltaEta_NLO[n]->Fill(qqDeltaEta_NLO, w);
                    hVEC_nrecoJet_NLO[n]->Fill(nrecoJet_NLO, w);
                    hVEC_genJet_Ht_NLO[n]->Fill(GenJet_Ht_NLO, w);
                    
                    hVECrecoPt1_q_NLO[n]->Fill(recoPt_q_NLO[0], w);
                    hVECrecoPt2_q_NLO[n]->Fill(recoPt_q_NLO[1], w);
                    for(int jet_idx = 0; jet_idx < 30; jet_idx++){
                        if(recoPt_q_NLO[jet_idx] > 20)  hVECrecoPt_q_NLO[n]->Fill(recoPt_q_NLO[jet_idx], w);
                    }
                   
                }

            }
            
            
            
//             if(recoJet_Mjj_NLO > 200) {
            if(recoJet_Mjj_NLO > 200 && recoMu_Mll_NLO>110 && selectionStep_NLO >= nCut-2) {
                    hVEC_Mll_NLO[nCut-1]->Fill(recoMu_Mll_NLO, w);            
                    hVEC_genMqq_NLO[nCut-1]->Fill(Mjj_NLO, w);
                    hVEC_recoMqq_NLO[nCut-1]->Fill(recoJet_Mjj_NLO, w);
                    hVEC_pt1q_NLO[nCut-1]->Fill(pt_q_NLO[0], w);
                    hVEC_pt2q_NLO[nCut-1]->Fill(pt_q_NLO[1], w);  
                    hVEC_nrecoJet_NLO[nCut-1]->Fill(nrecoJet_NLO, w);
                    hVEC_genJet_Ht_NLO[nCut-1]->Fill(GenJet_Ht_NLO, w);
                    hVECqqDeltaEta_NLO[nCut-1]->Fill(qqDeltaEta_NLO, w);
                    hVECrecoPt1_q_NLO[nCut-1]->Fill(recoPt_q_NLO[0], w);
                    hVECrecoPt2_q_NLO[nCut-1]->Fill(recoPt_q_NLO[1], w);
                    for(int jet_idx = 0; jet_idx < 30; jet_idx++){
                        if(recoPt_q_NLO[jet_idx] > 20)  hVECrecoPt_q_NLO[nCut-1]->Fill(recoPt_q_NLO[jet_idx], w);
                    }
                
            }
            
        }
        
        
        
        
        
        
        for (int entry=0; entry<nentries_LO;++entry){

            tree_LO->GetEntry(entry);
            
//             if (weight_NLO>-0.5) w = 1.;
//             else w = -1;     
            w = weight_LO;
            if (abs(weight_LO) > 2) continue;  
            
            
            
//              if (recoMu_Mll_LO < 55) continue;
//             if ((recoMu_Mll_LO < 75) || (recoMu_Mll_LO > 105)) continue;
//             if ((GenMll_LO < 75) || (GenMll_LO > 105)) continue;

                        
                        
            for(int n = 0; n < nCut; n++) {
                if (selectionStep_LO >= n) {
                    if (selectionStep_LO >= 3 && recoMu_Mll_LO<110) continue;
                    hVEC_Mll_LO[n]->Fill(recoMu_Mll_LO, w);            
//                     hVEC_Mll_LO[n]->Fill(GenMll_LO, w);            
                    hVEC_genMqq_LO[n]->Fill(Mjj_LO, w);
                    hVEC_recoMqq_LO[n]->Fill(recoJet_Mjj_LO, w);
                    hVEC_pt1q_LO[n]->Fill(pt_q_LO[0], w);
                    hVEC_pt2q_LO[n]->Fill(pt_q_LO[1], w);
                    hVECqqDeltaEta_LO[n]->Fill(qqDeltaEta_LO, w);
                    hVEC_nrecoJet_LO[n]->Fill(nrecoJet_LO, w);
                    hVEC_genJet_Ht_LO[n]->Fill(GenJet_Ht_LO, w);
                    
                    hVECrecoPt1_q_LO[n]->Fill(recoPt_q_LO[0], w);
                    hVECrecoPt2_q_LO[n]->Fill(recoPt_q_LO[1], w);
                    for(int jet_idx = 0; jet_idx < 30; jet_idx++){
                        if(recoPt_q_LO[jet_idx] > 20)  hVECrecoPt_q_LO[n]->Fill(recoPt_q_LO[jet_idx], w);
                    }
                    
                    
                    
                }
            }
            
            
            if(recoJet_Mjj_LO > 200 && recoMu_Mll_LO>110 && selectionStep_LO >= nCut-2) {
                    hVEC_Mll_LO[nCut-1]->Fill(recoMu_Mll_LO, w);            
                    hVEC_genMqq_LO[nCut-1]->Fill(Mjj_LO, w);
                    hVEC_recoMqq_LO[nCut-1]->Fill(recoJet_Mjj_LO, w);
                    hVEC_pt1q_LO[nCut-1]->Fill(pt_q_LO[0], w);
                    hVEC_pt2q_LO[nCut-1]->Fill(pt_q_LO[1], w);  
                    hVEC_nrecoJet_NLO[nCut-1]->Fill(nrecoJet_NLO, w);
                    hVEC_genJet_Ht_NLO[nCut-1]->Fill(GenJet_Ht_NLO, w);
                    hVECqqDeltaEta_LO[nCut-1]->Fill(qqDeltaEta_LO, w);
                    hVEC_genJet_Ht_LO[nCut-1]->Fill(GenJet_Ht_LO, w);
                    
                    hVECrecoPt1_q_LO[nCut-1]->Fill(recoPt_q_LO[0], w);
                    hVECrecoPt2_q_LO[nCut-1]->Fill(recoPt_q_LO[1], w);
                    for(int jet_idx = 0; jet_idx < 30; jet_idx++){
                        if(recoPt_q_LO[jet_idx] > 20)  hVECrecoPt_q_LO[nCut-1]->Fill(recoPt_q_LO[jet_idx], w);
                    }
                    
            }
            
            
            
            
        }
        
        
        
        
        
                
        float Xbottom = 0.65;
        float Ybottom = 0.7;
        float Xtop    = 0.89;
        float Ytop    = 0.89;
        TLegend *myLegend=new TLegend(Xbottom, Ybottom, Xtop, Ytop, "");
        myLegend->SetBorderSize(0);
        myLegend->SetFillStyle(0);
        myLegend->SetTextFont(42);
        myLegend->SetTextSize(0.04);
        myLegend->SetBorderSize(0);                  // without border
        myLegend->SetFillColorAlpha(1,0); 
        
        
        hVEC_Mll_NLO[0]->SetLineColor(2);
        if(nameSample.find("Inclusive")!=std::string::npos) {
        myLegend->AddEntry(hVEC_Mll_NLO[0], (nameSample+" NLO").c_str(),"l");
        myLegend->AddEntry(hVEC_Mll_LO[0], (nameSample+" LO").c_str(),"l");
        }
        
        if(nameSample.find("highMass")!=std::string::npos) {
        myLegend->AddEntry(hVEC_Mll_NLO[0], (nameSample+" NLO").c_str(),"l");
        myLegend->AddEntry(hVEC_Mll_LO[0], (nameSample+" LO").c_str(),"l");
        }
        
        
        
        
//         float normalization = 100.;
        double normalization_NLO = 100./hVEC_Mll_NLO[0]->Integral(0, hVEC_Mll_NLO[0]->GetXaxis()->GetNbins()+1);
        double normalization_LO  =  100./hVEC_Mll_LO[0]->Integral(0, hVEC_Mll_LO[0]->GetXaxis()->GetNbins()+1);
        
        
        
        
         
        canv->cd();
        gPad->SetLogy();     
        
        
        for(int n = 0; n < nCut; n++) {
            
                        
            stringstream ss;
            ss << n;
            string n_str = ss.str();
            
            if (n < 10) n_str = "0"+n_str;
                        
                        
            hVEC_Mll_NLO[n]->Scale(normalization_NLO);
            hVEC_genMqq_NLO[n]->Scale(normalization_NLO);
            hVEC_recoMqq_NLO[n]->Scale(normalization_NLO);
            hVEC_pt1q_NLO[n]->Scale(normalization_NLO);
            hVEC_pt2q_NLO[n]->Scale(normalization_NLO);
            hVEC_nrecoJet_NLO[n]->Scale(normalization_NLO);
            hVEC_genJet_Ht_NLO[n]->Scale(normalization_NLO);
            hVECqqDeltaEta_NLO[n]->Scale(normalization_NLO);
            hVECrecoPt_q_NLO[n]->Scale(normalization_NLO);
            hVECrecoPt1_q_NLO[n]->Scale(normalization_NLO);
            hVECrecoPt2_q_NLO[n]->Scale(normalization_NLO);
            
            
            hVEC_Mll_LO[n]->Scale(normalization_LO);
            hVEC_genMqq_LO[n]->Scale(normalization_LO);
            hVEC_recoMqq_LO[n]->Scale(normalization_LO);
            hVEC_pt1q_LO[n]->Scale(normalization_LO);
            hVEC_pt2q_LO[n]->Scale(normalization_LO);
            hVEC_nrecoJet_LO[n]->Scale(normalization_LO);
            hVEC_genJet_Ht_LO[n]->Scale(normalization_LO);
            hVECqqDeltaEta_LO[n]->Scale(normalization_LO);
            hVECrecoPt_q_LO[n]->Scale(normalization_LO);
            hVECrecoPt1_q_LO[n]->Scale(normalization_LO);
            hVECrecoPt2_q_LO[n]->Scale(normalization_LO);
            
            

            DrawSame_and_Save(canv, hVEC_Mll_LO[n], hVEC_Mll_NLO[n], myLegend, ("figureOgniTaglio/hMll_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVEC_genMqq_LO[n], hVEC_genMqq_NLO[n], myLegend, ("figureOgniTaglio/hMqqGen_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVEC_recoMqq_LO[n], hVEC_recoMqq_NLO[n], myLegend, ("figureOgniTaglio/hMqqReco_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVEC_pt1q_LO[n], hVEC_pt1q_NLO[n], myLegend, ("figureOgniTaglio/hpt1q_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVEC_pt2q_LO[n], hVEC_pt2q_NLO[n], myLegend, ("figureOgniTaglio/hpt2q_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVECrecoPt_q_LO[n], hVECrecoPt_q_NLO[n], myLegend, ("figureOgniTaglio/hrecoPt_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVECrecoPt1_q_LO[n], hVECrecoPt1_q_NLO[n], myLegend, ("figureOgniTaglio/hrecoPt1_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVECrecoPt2_q_LO[n], hVECrecoPt2_q_NLO[n], myLegend, ("figureOgniTaglio/hrecoPt2_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVECqqDeltaEta_LO[n], hVECqqDeltaEta_NLO[n], myLegend, ("figureOgniTaglio/hqqDeltaEta_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVEC_nrecoJet_LO[n], hVEC_nrecoJet_NLO[n], myLegend, ("figureOgniTaglio/hnrecoJet_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVEC_genJet_Ht_LO[n], hVEC_genJet_Ht_NLO[n], myLegend, ("figureOgniTaglio/hgenJetHt_"+n_str).c_str(), nameSample);

        
        }

            
        
        
//         gPad->SetLogy(0);
//         gStyle->SetOptStat(0000);
//         hMll_NLO->GetXaxis()->SetTitle("Mll [GeV]");
//         hMll_NLO->GetYaxis()->SetTitle("NLO/LO");
//         hMll_NLO->GetYaxis()->SetTitleSize(0.05);
//         hMll_NLO->GetYaxis()->SetTitleOffset(1.);
//         
//         hMll_NLO->GetYaxis()->SetRangeUser(0.9, 1.1);
//         hMll_NLO->Divide(hMll_LO);
//         hMll_NLO->Draw();
//         canv->Print("figure/ratio.png");




}








