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


void DrawSame_and_Save(TCanvas * canv, TH1 * histo1, TH1 * histo2,TLegend * leg,std::string name, std::string nameSample) {
    canv->cd(1);
    gStyle->SetOptStat(0000);
    
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
    double ratio = integral1/integral2;

//     std::cout << error << " \t " << error1 << " \t " << error2 << std::endl;
                
    stringstream ss_ratio;
    ss_ratio << std::setprecision(2) << ratio;
    string ratio_str = ss_ratio.str();
    
    stringstream ss_error;
    ss_error << std::setprecision(2) << error;
//     ss_error <<  error;
    string error_str = ss_error.str();
    
    
    
    
    float yt2 = 0.2;
    float xt2 = 0.25;
    TLatex * t2 = new TLatex(xt2,yt2 ,("LO/NLO="+ratio_str+" +- "+error_str).c_str());
    t2->SetNDC();
    t2->SetTextAlign(22);
    t2->SetTextSize(0.04);
    t2->Draw();
    
    
    
    
    
    
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
        
        
        
//         TFile * f_NLO = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_InclusiveSum_NLO.root");
//         TFile * f_LO  = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_InclusiveSum_LO.root");
        
        TFile * f_NLO = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_HighMassSum_NLO.root");
        TFile * f_LO  = new TFile ("/scratch/mandorli/Hmumu/AnalyzerMiniAOD/CMSSW_8_0_28/src/AnalyzerMiniAOD/test_HighMassSum_LO.root");
        
        
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
            mll_max = 120;
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
        
        float ptMin = 0;
        float ptMax = 120;
        std::vector<TH1F*> hVEC_pt1q_NLO;
        std::vector<TH1F*> hVEC_pt1q_LO; 
        std::vector<TH1F*> hVEC_pt2q_NLO;
        std::vector<TH1F*> hVEC_pt2q_LO;
        
        
//         std::vector<std::string> cutNames = {"no cut", "#jet > 1", "#mu = 2", "mll > 110", "mll < 145", "Mjj > 200", "pT_1q >35", "pT_2q >25", "pT_1mu >30", "pT_2mu >10", "|eta_1mu| <2.4", "|eta_2mu| <2.4", "   ", "|eta_qq| <2.5", "z*<2.5", "Mqq > 200"};
//         std::vector<std::string> cutNames = {"no cut", "#jet > 1", "#mu = 2", "", "mll < 145", "", "pT_1q >35", "pT_2q >25", "pT_1mu >30", "pT_2mu >10", "|eta_1mu| <2.4", "|eta_2mu| <2.4", "   ", "|eta_qq| <2.5", "z*<2.5", "Mqq > 200"};
        std::vector<std::string> cutNames = {"no cut", "#jet > 1", "#mu = 2", "", "mll < 145", "", "pT_1q >35", "pT_2q >25", "pT_1mu >30", "pT_2mu >10", "|eta_1mu| <2.4", "|eta_2mu| <2.4", "   ", "|eta_qq| <2.5", "preselection w/o Mqq cut", "preselection + Mqq > 200"};
        
        
        int nCut = 16;
        for(int n = 0; n < nCut; n++) {
            
            stringstream ss;
            ss << n;
            string n_str = ss.str();

            if (n < 10) n_str = "0"+n_str;

            TH1F * hMll_NLO = new TH1F (("hMll_NLO"+n_str).c_str(), (cutNames[n]+";Mll [GeV];").c_str(), 40, mll_min, mll_max); 
            TH1F * hMll_LO = new TH1F (("hMll_LO"+n_str).c_str(), (cutNames[n]+";Mll [GeV];").c_str(), 40, mll_min, mll_max); 
            hMll_NLO->Sumw2();
            hMll_LO->Sumw2();
            
            
            TH1F * hgenMqq_NLO = new TH1F (("hgenMqq_NLO"+n_str).c_str(), (cutNames[n]+";gen Mqq [GeV];").c_str(), 40, 0, 400); 
            TH1F * hgenMqq_LO = new TH1F (("hgenMqq_LO"+n_str).c_str(), (cutNames[n]+";gen Mqq [GeV];").c_str(), 40, 0, 400); 
            hgenMqq_NLO->Sumw2();
            hgenMqq_LO->Sumw2();
            
            
            TH1F * hrecoMqq_NLO = new TH1F (("hrecoMqq_NLO"+n_str).c_str(), (cutNames[n]+";reco Mqq [GeV];").c_str(), 40, 0, 400); 
            TH1F * hrecoMqq_LO = new TH1F (("hrecoMqq_LO"+n_str).c_str(), (cutNames[n]+";reco Mqq [GeV];").c_str(), 40, 0, 400); 
            hrecoMqq_NLO->Sumw2();
            hrecoMqq_LO->Sumw2();
            

            TH1F * hpt1q_NLO = new TH1F (("hpt1q_NLO"+n_str).c_str(), (cutNames[n]+";pt(1q) [GeV];").c_str(), 40, ptMin, ptMax); 
            TH1F * hpt1q_LO  = new TH1F (("hpt1q_LO"+n_str).c_str(), (cutNames[n]+";pt(1q) [GeV];").c_str(), 40, ptMin, ptMax); 
            hpt1q_NLO->Sumw2();
            hpt1q_LO->Sumw2(); 
            
            
            TH1F * hpt2q_NLO = new TH1F (("hpt2q_NLO"+n_str).c_str(), (cutNames[n]+";pt(2q) [GeV];").c_str(), 40, ptMin, ptMax); 
            TH1F * hpt2q_LO  = new TH1F (("hpt2q_LO"+n_str).c_str(), (cutNames[n]+";pt(2q) [GeV];").c_str(), 40, ptMin, ptMax); 
            hpt2q_NLO->Sumw2();
            hpt2q_LO->Sumw2();

            
            
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
        float pt_q_NLO[30]={};
        float pt_q_LO[30]={};

        int selectionStep_NLO=0;
        int selectionStep_LO=0;

                        
        tree_NLO->SetBranchAddress("GenMu_Mll", &GenMll_NLO);
        tree_NLO->SetBranchAddress("recoMu_Mll", &recoMu_Mll_NLO);
        tree_NLO->SetBranchAddress("weight", &weight_NLO);
        tree_NLO->SetBranchAddress("GenJet_Mjj", &Mjj_NLO);
        tree_NLO->SetBranchAddress("GenJet_pt", &pt_q_NLO);
        tree_NLO->SetBranchAddress("recoJet_Mjj", &recoJet_Mjj_NLO);
        tree_NLO->SetBranchAddress("selectionStep", &selectionStep_NLO);
        
        tree_LO->SetBranchAddress("GenMu_Mll", &GenMll_LO);
        tree_LO->SetBranchAddress("recoMu_Mll", &recoMu_Mll_LO);
        tree_LO->SetBranchAddress("weight", &weight_LO);
        tree_LO->SetBranchAddress("GenJet_Mjj", &Mjj_LO);
        tree_LO->SetBranchAddress("GenJet_pt", &pt_q_LO);
        tree_LO->SetBranchAddress("recoJet_Mjj", &recoJet_Mjj_LO);
        tree_LO->SetBranchAddress("selectionStep", &selectionStep_LO);
        


        int total = 0;
        float w=1;

        for (int entry=0; entry<nentries_NLO;++entry){

            tree_NLO->GetEntry(entry);
              
/*            if (weight_NLO>-0.5) w = 1.;
            else w = -1; */         
            w = weight_NLO;

//             if ((recoMu_Mll_NLO < 75) || (recoMu_Mll_NLO > 105)) continue;
//             if ((GenMll_NLO < 75) || (GenMll_NLO > 105)) continue;

            for(int n = 0; n < nCut-1; n++) {
                if (selectionStep_NLO >= n) {
                    hVEC_Mll_NLO[n]->Fill(recoMu_Mll_NLO, w);
//                     hVEC_Mll_NLO[n]->Fill(GenMll_NLO, w);
                    hVEC_genMqq_NLO[n]->Fill(Mjj_NLO, w);
                    hVEC_recoMqq_NLO[n]->Fill(recoJet_Mjj_NLO, w);
                    hVEC_pt1q_NLO[n]->Fill(pt_q_NLO[0], w);
                    hVEC_pt2q_NLO[n]->Fill(pt_q_NLO[1], w);
                }

            }
            
            
            
//             if(recoJet_Mjj_NLO > 200) {
            if(recoJet_Mjj_NLO > 200 && selectionStep_NLO >= nCut-2) {
                    hVEC_Mll_NLO[nCut-1]->Fill(recoMu_Mll_NLO, w);            
                    hVEC_genMqq_NLO[nCut-1]->Fill(Mjj_NLO, w);
                    hVEC_recoMqq_NLO[nCut-1]->Fill(recoJet_Mjj_NLO, w);
                    hVEC_pt1q_NLO[nCut-1]->Fill(pt_q_NLO[0], w);
                    hVEC_pt2q_NLO[nCut-1]->Fill(pt_q_NLO[1], w);  
            }
            
        }
        
        
        
        
        
        
        for (int entry=0; entry<nentries_LO;++entry){

            tree_LO->GetEntry(entry);
            
//             if (weight_NLO>-0.5) w = 1.;
//             else w = -1;     
            w = weight_LO;
            
            
//             if ((recoMu_Mll_LO < 75) || (recoMu_Mll_LO > 105)) continue;
//             if ((GenMll_LO < 75) || (GenMll_LO > 105)) continue;

                        
                        
            for(int n = 0; n < nCut; n++) {
                if (selectionStep_LO >= n) {
                    hVEC_Mll_LO[n]->Fill(recoMu_Mll_LO, w);            
//                     hVEC_Mll_LO[n]->Fill(GenMll_LO, w);            
                    hVEC_genMqq_LO[n]->Fill(Mjj_LO, w);
                    hVEC_recoMqq_LO[n]->Fill(recoJet_Mjj_LO, w);
                    hVEC_pt1q_LO[n]->Fill(pt_q_LO[0], w);
                    hVEC_pt2q_LO[n]->Fill(pt_q_LO[1], w);
                }
            }
            
            
            if(recoJet_Mjj_LO > 200 && selectionStep_LO >= nCut-2) {
                    hVEC_Mll_LO[nCut-1]->Fill(recoMu_Mll_LO, w);            
                    hVEC_genMqq_LO[nCut-1]->Fill(Mjj_LO, w);
                    hVEC_recoMqq_LO[nCut-1]->Fill(recoJet_Mjj_LO, w);
                    hVEC_pt1q_LO[nCut-1]->Fill(pt_q_LO[0], w);
                    hVEC_pt2q_LO[nCut-1]->Fill(pt_q_LO[1], w);  
            }
            
            
            
            
        }
        
        
        
        
        
                
        float Xbottom = 0.1;
        float Ybottom = 0.7;
        float Xtop    = 0.35;
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
            
            hVEC_Mll_LO[n]->Scale(normalization_LO);
            hVEC_genMqq_LO[n]->Scale(normalization_LO);
            hVEC_recoMqq_LO[n]->Scale(normalization_LO);
            hVEC_pt1q_LO[n]->Scale(normalization_LO);
            hVEC_pt2q_LO[n]->Scale(normalization_LO);

        

            DrawSame_and_Save(canv, hVEC_Mll_LO[n], hVEC_Mll_NLO[n], myLegend, ("figureOgniTaglio/hMll_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVEC_genMqq_LO[n], hVEC_genMqq_NLO[n], myLegend, ("figureOgniTaglio/hMqqGen_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVEC_recoMqq_LO[n], hVEC_recoMqq_NLO[n], myLegend, ("figureOgniTaglio/hMqqReco_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVEC_pt1q_LO[n], hVEC_pt1q_NLO[n], myLegend, ("figureOgniTaglio/hpt1q_"+n_str).c_str(), nameSample);
            DrawSame_and_Save(canv, hVEC_pt2q_LO[n], hVEC_pt2q_NLO[n], myLegend, ("figureOgniTaglio/hpt2q_"+n_str).c_str(), nameSample);

        
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








