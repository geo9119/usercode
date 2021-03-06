sampleDataSet = '/QCD_Pt-300to470_TuneZ2_7TeV_pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM'
sampleCMSEnergy = 7000

sampleRelease = "CMSSW_4_2_2_patch2" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_4_2_7" # release used to create new files with

sampleNumEvents = 6432669

sampleXSec = 1170.0 # cross-section times filter efficiency (pb)

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START42_V13::All'
sampleHLTProcess = '*'

sampleBaseDir = "root://xrootd.rcac.purdue.edu//store/user/demattia/longlived/"+sampleProcessRelease+"/QCDem300"

sampleRecoFiles = [ ]

samplePatFiles = [
  sampleBaseDir+"/pat/PATtuple_1_1_Egr.root",
  sampleBaseDir+"/pat/PATtuple_2_1_wJK.root",
  sampleBaseDir+"/pat/PATtuple_3_1_e5d.root",
  sampleBaseDir+"/pat/PATtuple_4_1_XSo.root",
  sampleBaseDir+"/pat/PATtuple_5_1_YSh.root",
  sampleBaseDir+"/pat/PATtuple_6_1_PJR.root",
  sampleBaseDir+"/pat/PATtuple_7_1_1hb.root",
  sampleBaseDir+"/pat/PATtuple_8_1_vQ2.root",
  sampleBaseDir+"/pat/PATtuple_9_1_z81.root",
  sampleBaseDir+"/pat/PATtuple_10_1_Xrt.root",
  sampleBaseDir+"/pat/PATtuple_11_1_va9.root",
  sampleBaseDir+"/pat/PATtuple_12_1_46X.root",
  sampleBaseDir+"/pat/PATtuple_13_1_DYO.root",
  sampleBaseDir+"/pat/PATtuple_14_1_PvL.root",
  sampleBaseDir+"/pat/PATtuple_15_1_Ph4.root",
  sampleBaseDir+"/pat/PATtuple_16_1_ZVg.root",
  sampleBaseDir+"/pat/PATtuple_17_1_76K.root",
  sampleBaseDir+"/pat/PATtuple_18_1_k44.root",
  sampleBaseDir+"/pat/PATtuple_19_0_i9W.root",
  sampleBaseDir+"/pat/PATtuple_20_0_W6h.root",
  sampleBaseDir+"/pat/PATtuple_21_0_1ui.root",
  sampleBaseDir+"/pat/PATtuple_22_0_hai.root",
  sampleBaseDir+"/pat/PATtuple_23_0_B1k.root",
  sampleBaseDir+"/pat/PATtuple_24_0_6bX.root",
  sampleBaseDir+"/pat/PATtuple_25_0_JNk.root",
  sampleBaseDir+"/pat/PATtuple_26_0_5K8.root",
  sampleBaseDir+"/pat/PATtuple_27_0_2RO.root",
  sampleBaseDir+"/pat/PATtuple_28_0_GOV.root",
  sampleBaseDir+"/pat/PATtuple_29_0_mla.root",
  sampleBaseDir+"/pat/PATtuple_30_0_oCf.root",
  sampleBaseDir+"/pat/PATtuple_31_0_9z1.root",
  sampleBaseDir+"/pat/PATtuple_32_0_vfl.root",
  sampleBaseDir+"/pat/PATtuple_33_0_Yma.root",
  sampleBaseDir+"/pat/PATtuple_34_0_TwY.root",
  sampleBaseDir+"/pat/PATtuple_35_0_eEB.root",
  sampleBaseDir+"/pat/PATtuple_36_0_afP.root",
  sampleBaseDir+"/pat/PATtuple_37_0_Lul.root",
  sampleBaseDir+"/pat/PATtuple_38_0_TwR.root",
  sampleBaseDir+"/pat/PATtuple_39_0_Atp.root",
  sampleBaseDir+"/pat/PATtuple_40_0_GMN.root",
  sampleBaseDir+"/pat/PATtuple_41_0_7Ud.root",
  sampleBaseDir+"/pat/PATtuple_42_0_rOI.root",
  sampleBaseDir+"/pat/PATtuple_43_0_Yo4.root",
  sampleBaseDir+"/pat/PATtuple_44_0_hjc.root",
  sampleBaseDir+"/pat/PATtuple_45_0_M2t.root",
  sampleBaseDir+"/pat/PATtuple_46_0_Exg.root",
  sampleBaseDir+"/pat/PATtuple_47_0_4zy.root",
  sampleBaseDir+"/pat/PATtuple_48_0_YqC.root",
  sampleBaseDir+"/pat/PATtuple_49_0_vEj.root",
  sampleBaseDir+"/pat/PATtuple_50_0_zib.root",
  sampleBaseDir+"/pat/PATtuple_51_0_xrh.root",
  sampleBaseDir+"/pat/PATtuple_52_0_TYN.root",
  sampleBaseDir+"/pat/PATtuple_53_0_NGa.root",
  sampleBaseDir+"/pat/PATtuple_54_0_kc1.root",
  sampleBaseDir+"/pat/PATtuple_55_0_m0P.root",
  sampleBaseDir+"/pat/PATtuple_56_0_9JX.root",
  sampleBaseDir+"/pat/PATtuple_57_0_RJx.root",
  sampleBaseDir+"/pat/PATtuple_58_0_IDv.root",
  sampleBaseDir+"/pat/PATtuple_59_0_XV5.root",
  sampleBaseDir+"/pat/PATtuple_60_0_J5D.root",
  sampleBaseDir+"/pat/PATtuple_61_0_Rxs.root",
  sampleBaseDir+"/pat/PATtuple_62_0_3JP.root",
  sampleBaseDir+"/pat/PATtuple_63_0_4DB.root",
  sampleBaseDir+"/pat/PATtuple_64_0_syg.root",
  sampleBaseDir+"/pat/PATtuple_65_0_s2p.root",
  sampleBaseDir+"/pat/PATtuple_66_0_UIN.root",
  sampleBaseDir+"/pat/PATtuple_67_0_1zd.root",
  sampleBaseDir+"/pat/PATtuple_68_0_43s.root",
  sampleBaseDir+"/pat/PATtuple_69_0_5P7.root",
  sampleBaseDir+"/pat/PATtuple_70_0_fEq.root",
  sampleBaseDir+"/pat/PATtuple_71_0_A6U.root",
  sampleBaseDir+"/pat/PATtuple_72_0_n43.root",
  sampleBaseDir+"/pat/PATtuple_73_0_XP6.root",
  sampleBaseDir+"/pat/PATtuple_74_0_F6H.root",
  sampleBaseDir+"/pat/PATtuple_75_0_XNC.root",
  sampleBaseDir+"/pat/PATtuple_76_0_yK8.root",
  sampleBaseDir+"/pat/PATtuple_77_0_Y5j.root",
  sampleBaseDir+"/pat/PATtuple_78_0_tnQ.root",
  sampleBaseDir+"/pat/PATtuple_79_0_GRL.root",
  sampleBaseDir+"/pat/PATtuple_80_0_fs5.root",
  sampleBaseDir+"/pat/PATtuple_81_0_upX.root",
  sampleBaseDir+"/pat/PATtuple_82_0_QCr.root",
  sampleBaseDir+"/pat/PATtuple_83_0_coV.root",
  sampleBaseDir+"/pat/PATtuple_84_0_p2x.root",
  sampleBaseDir+"/pat/PATtuple_85_0_uLw.root",
  sampleBaseDir+"/pat/PATtuple_86_0_FqN.root",
  sampleBaseDir+"/pat/PATtuple_87_0_JXu.root",
  sampleBaseDir+"/pat/PATtuple_88_0_icn.root",
  sampleBaseDir+"/pat/PATtuple_89_0_Bfg.root",
  sampleBaseDir+"/pat/PATtuple_90_0_6yw.root",
  sampleBaseDir+"/pat/PATtuple_91_0_Pif.root",
  sampleBaseDir+"/pat/PATtuple_92_0_l4r.root",
  sampleBaseDir+"/pat/PATtuple_93_0_ai4.root",
  sampleBaseDir+"/pat/PATtuple_94_0_IvM.root",
  sampleBaseDir+"/pat/PATtuple_95_0_2pD.root",
  sampleBaseDir+"/pat/PATtuple_96_0_8Jk.root",
  sampleBaseDir+"/pat/PATtuple_97_0_96W.root",
  sampleBaseDir+"/pat/PATtuple_98_0_QMd.root",
  sampleBaseDir+"/pat/PATtuple_99_0_zwt.root",
  sampleBaseDir+"/pat/PATtuple_100_0_0aX.root",
  sampleBaseDir+"/pat/PATtuple_101_0_pKs.root",
  sampleBaseDir+"/pat/PATtuple_102_0_Tmr.root",
  sampleBaseDir+"/pat/PATtuple_103_0_h56.root",
  sampleBaseDir+"/pat/PATtuple_104_0_rBD.root",
  sampleBaseDir+"/pat/PATtuple_105_0_giG.root",
  sampleBaseDir+"/pat/PATtuple_106_0_USY.root",
  sampleBaseDir+"/pat/PATtuple_107_0_Ij4.root",
  sampleBaseDir+"/pat/PATtuple_108_0_4dT.root",
  sampleBaseDir+"/pat/PATtuple_109_0_HxM.root",
  sampleBaseDir+"/pat/PATtuple_110_0_3Ni.root",
  sampleBaseDir+"/pat/PATtuple_111_0_Dmf.root",
  sampleBaseDir+"/pat/PATtuple_112_0_8i8.root",
  sampleBaseDir+"/pat/PATtuple_113_0_Rxt.root",
  sampleBaseDir+"/pat/PATtuple_114_0_hZa.root",
  sampleBaseDir+"/pat/PATtuple_115_0_gSA.root",
  sampleBaseDir+"/pat/PATtuple_116_0_vpl.root",
  sampleBaseDir+"/pat/PATtuple_117_0_nuK.root",
  sampleBaseDir+"/pat/PATtuple_118_0_Hvt.root",
  sampleBaseDir+"/pat/PATtuple_119_0_hPC.root",
  sampleBaseDir+"/pat/PATtuple_120_0_kYl.root",
  sampleBaseDir+"/pat/PATtuple_121_0_oxm.root",
  sampleBaseDir+"/pat/PATtuple_122_0_d8z.root",
  sampleBaseDir+"/pat/PATtuple_123_0_kJI.root",
  sampleBaseDir+"/pat/PATtuple_124_0_Mh1.root",
  sampleBaseDir+"/pat/PATtuple_125_0_oha.root",
  sampleBaseDir+"/pat/PATtuple_126_0_s2t.root",
  sampleBaseDir+"/pat/PATtuple_127_0_lsj.root",
  sampleBaseDir+"/pat/PATtuple_128_0_GAA.root",
  sampleBaseDir+"/pat/PATtuple_129_0_qHH.root",
  sampleBaseDir+"/pat/PATtuple_130_0_dBR.root",
  sampleBaseDir+"/pat/PATtuple_131_0_kHk.root",
  sampleBaseDir+"/pat/PATtuple_132_0_29L.root",
  sampleBaseDir+"/pat/PATtuple_133_0_7DR.root",
  sampleBaseDir+"/pat/PATtuple_134_0_gdz.root",
  sampleBaseDir+"/pat/PATtuple_135_0_Efm.root",
  sampleBaseDir+"/pat/PATtuple_136_0_tK4.root",
  sampleBaseDir+"/pat/PATtuple_137_0_Cl0.root",
  sampleBaseDir+"/pat/PATtuple_138_0_Gd6.root",
  sampleBaseDir+"/pat/PATtuple_139_0_Ggj.root",
  sampleBaseDir+"/pat/PATtuple_140_0_Qu2.root",
  sampleBaseDir+"/pat/PATtuple_141_0_AJj.root",
  sampleBaseDir+"/pat/PATtuple_142_0_0mH.root",
  sampleBaseDir+"/pat/PATtuple_143_0_BRw.root",
  sampleBaseDir+"/pat/PATtuple_144_0_9Cx.root",
  sampleBaseDir+"/pat/PATtuple_145_0_KSa.root",
  sampleBaseDir+"/pat/PATtuple_146_0_Gv0.root",
  sampleBaseDir+"/pat/PATtuple_147_0_UGK.root",
  sampleBaseDir+"/pat/PATtuple_148_0_RTj.root",
  sampleBaseDir+"/pat/PATtuple_149_0_TxE.root",
  sampleBaseDir+"/pat/PATtuple_150_0_Fdy.root",
  sampleBaseDir+"/pat/PATtuple_151_0_BVq.root",
  sampleBaseDir+"/pat/PATtuple_152_0_j3S.root",
  sampleBaseDir+"/pat/PATtuple_153_0_vbt.root",
  sampleBaseDir+"/pat/PATtuple_154_0_RKn.root",
  sampleBaseDir+"/pat/PATtuple_155_0_zWY.root",
  sampleBaseDir+"/pat/PATtuple_156_0_bKI.root",
  sampleBaseDir+"/pat/PATtuple_157_0_nmf.root",
  sampleBaseDir+"/pat/PATtuple_158_0_Pp3.root",
  sampleBaseDir+"/pat/PATtuple_159_0_grH.root",
  sampleBaseDir+"/pat/PATtuple_160_0_WPg.root",
  sampleBaseDir+"/pat/PATtuple_161_0_wws.root",
  sampleBaseDir+"/pat/PATtuple_162_0_Csl.root",
  sampleBaseDir+"/pat/PATtuple_163_0_iGR.root",
  sampleBaseDir+"/pat/PATtuple_164_0_aWn.root",
  sampleBaseDir+"/pat/PATtuple_165_1_2Nk.root",
  sampleBaseDir+"/pat/PATtuple_166_1_uSE.root",
  sampleBaseDir+"/pat/PATtuple_167_1_k7x.root",
  sampleBaseDir+"/pat/PATtuple_168_1_JPJ.root",
  sampleBaseDir+"/pat/PATtuple_169_0_1WR.root",
  sampleBaseDir+"/pat/PATtuple_170_0_wQn.root",
  sampleBaseDir+"/pat/PATtuple_171_0_T83.root",
  sampleBaseDir+"/pat/PATtuple_172_0_m52.root",
  sampleBaseDir+"/pat/PATtuple_173_0_oc0.root",
  sampleBaseDir+"/pat/PATtuple_174_0_Afs.root",
  sampleBaseDir+"/pat/PATtuple_175_0_OiZ.root",
  sampleBaseDir+"/pat/PATtuple_176_0_sxQ.root",
  sampleBaseDir+"/pat/PATtuple_177_0_Qel.root",
  sampleBaseDir+"/pat/PATtuple_178_0_Vfp.root",
  sampleBaseDir+"/pat/PATtuple_179_0_m9N.root",
  sampleBaseDir+"/pat/PATtuple_180_0_0A4.root",
  sampleBaseDir+"/pat/PATtuple_181_0_zYn.root",
  sampleBaseDir+"/pat/PATtuple_182_0_mD8.root",
  sampleBaseDir+"/pat/PATtuple_183_0_a98.root",
  sampleBaseDir+"/pat/PATtuple_184_0_vOc.root",
  sampleBaseDir+"/pat/PATtuple_185_0_cmW.root",
  sampleBaseDir+"/pat/PATtuple_186_0_lCY.root",
  sampleBaseDir+"/pat/PATtuple_187_0_C8k.root",
  sampleBaseDir+"/pat/PATtuple_188_0_k89.root",
  sampleBaseDir+"/pat/PATtuple_189_0_311.root",
  sampleBaseDir+"/pat/PATtuple_190_0_2GE.root",
  sampleBaseDir+"/pat/PATtuple_191_0_0FK.root",
  sampleBaseDir+"/pat/PATtuple_192_0_E7w.root",
  sampleBaseDir+"/pat/PATtuple_193_0_LLJ.root",
  sampleBaseDir+"/pat/PATtuple_194_0_A38.root",
  sampleBaseDir+"/pat/PATtuple_195_0_d4m.root",
  sampleBaseDir+"/pat/PATtuple_196_0_mU9.root",
  sampleBaseDir+"/pat/PATtuple_197_0_LZf.root",
  sampleBaseDir+"/pat/PATtuple_198_0_Q1J.root",
  sampleBaseDir+"/pat/PATtuple_199_0_8aE.root",
  sampleBaseDir+"/pat/PATtuple_200_0_vAj.root",
  sampleBaseDir+"/pat/PATtuple_201_0_e0E.root",
  sampleBaseDir+"/pat/PATtuple_202_0_Ncd.root",
  sampleBaseDir+"/pat/PATtuple_203_0_Qe8.root",
  sampleBaseDir+"/pat/PATtuple_204_0_A46.root",
  sampleBaseDir+"/pat/PATtuple_205_0_fz0.root",
  sampleBaseDir+"/pat/PATtuple_206_0_jiV.root",
  sampleBaseDir+"/pat/PATtuple_207_0_XD5.root",
  sampleBaseDir+"/pat/PATtuple_208_0_RNL.root",
  sampleBaseDir+"/pat/PATtuple_209_0_2Nu.root",
  sampleBaseDir+"/pat/PATtuple_210_0_sKk.root",
  sampleBaseDir+"/pat/PATtuple_211_0_nHZ.root",
  sampleBaseDir+"/pat/PATtuple_212_0_Srg.root",
  sampleBaseDir+"/pat/PATtuple_213_0_3Cs.root",
  sampleBaseDir+"/pat/PATtuple_214_0_K4o.root",
  sampleBaseDir+"/pat/PATtuple_215_0_VpG.root",
  sampleBaseDir+"/pat/PATtuple_216_0_Dz9.root",
  sampleBaseDir+"/pat/PATtuple_217_0_KIg.root",
  sampleBaseDir+"/pat/PATtuple_218_0_S8W.root",
  sampleBaseDir+"/pat/PATtuple_219_0_ikW.root",
  sampleBaseDir+"/pat/PATtuple_220_0_4oC.root",
  sampleBaseDir+"/pat/PATtuple_221_0_nIO.root",
  sampleBaseDir+"/pat/PATtuple_222_0_oQX.root",
  sampleBaseDir+"/pat/PATtuple_223_1_dsU.root",
  sampleBaseDir+"/pat/PATtuple_224_1_JgR.root",
  sampleBaseDir+"/pat/PATtuple_225_1_cRq.root",
  sampleBaseDir+"/pat/PATtuple_226_1_Z7h.root",
  sampleBaseDir+"/pat/PATtuple_227_1_o14.root",
  sampleBaseDir+"/pat/PATtuple_228_1_jyN.root",
  sampleBaseDir+"/pat/PATtuple_229_1_l5m.root",
  sampleBaseDir+"/pat/PATtuple_230_1_hQS.root",
  sampleBaseDir+"/pat/PATtuple_231_1_YIm.root",
  sampleBaseDir+"/pat/PATtuple_232_1_bVA.root",
  sampleBaseDir+"/pat/PATtuple_233_1_RBV.root",
  sampleBaseDir+"/pat/PATtuple_234_1_QEV.root",
  sampleBaseDir+"/pat/PATtuple_235_1_Zwh.root",
  sampleBaseDir+"/pat/PATtuple_236_1_HPW.root",
  sampleBaseDir+"/pat/PATtuple_237_1_Vm6.root",
  sampleBaseDir+"/pat/PATtuple_238_1_ZO5.root",
  sampleBaseDir+"/pat/PATtuple_239_1_G3O.root",
  sampleBaseDir+"/pat/PATtuple_240_1_brJ.root",
  sampleBaseDir+"/pat/PATtuple_241_1_CQ6.root",
  sampleBaseDir+"/pat/PATtuple_242_1_dsK.root",
  sampleBaseDir+"/pat/PATtuple_243_1_2eS.root",
  sampleBaseDir+"/pat/PATtuple_244_1_BEq.root",
  sampleBaseDir+"/pat/PATtuple_245_1_vqv.root",
  sampleBaseDir+"/pat/PATtuple_246_1_Pff.root",
  sampleBaseDir+"/pat/PATtuple_247_1_1jA.root",
  sampleBaseDir+"/pat/PATtuple_248_1_YqV.root",
  sampleBaseDir+"/pat/PATtuple_249_1_gEW.root",
  sampleBaseDir+"/pat/PATtuple_250_1_JDF.root",
  sampleBaseDir+"/pat/PATtuple_251_1_QCk.root",
  sampleBaseDir+"/pat/PATtuple_252_1_7gm.root",
  sampleBaseDir+"/pat/PATtuple_253_1_gdb.root",
  sampleBaseDir+"/pat/PATtuple_254_1_uyV.root",
  sampleBaseDir+"/pat/PATtuple_255_1_BhF.root",
  sampleBaseDir+"/pat/PATtuple_256_1_sig.root",
  sampleBaseDir+"/pat/PATtuple_257_1_UEw.root",
  sampleBaseDir+"/pat/PATtuple_258_1_i3t.root",
  sampleBaseDir+"/pat/PATtuple_259_1_BoC.root",
  sampleBaseDir+"/pat/PATtuple_260_1_ony.root",
  sampleBaseDir+"/pat/PATtuple_261_1_VUx.root",
  sampleBaseDir+"/pat/PATtuple_262_1_js8.root",
  sampleBaseDir+"/pat/PATtuple_263_1_FVk.root",
  sampleBaseDir+"/pat/PATtuple_264_1_2WS.root",
  sampleBaseDir+"/pat/PATtuple_265_1_DXh.root",
  sampleBaseDir+"/pat/PATtuple_266_1_Fx3.root",
  sampleBaseDir+"/pat/PATtuple_267_1_8Yi.root",
  sampleBaseDir+"/pat/PATtuple_268_1_zf1.root",
  sampleBaseDir+"/pat/PATtuple_269_1_VPn.root",
  sampleBaseDir+"/pat/PATtuple_270_1_Eai.root",
  sampleBaseDir+"/pat/PATtuple_271_1_Pa6.root",
  sampleBaseDir+"/pat/PATtuple_272_1_6mP.root",
  sampleBaseDir+"/pat/PATtuple_273_1_ZKc.root",
  sampleBaseDir+"/pat/PATtuple_274_1_yKM.root",
  sampleBaseDir+"/pat/PATtuple_275_1_iAv.root",
  sampleBaseDir+"/pat/PATtuple_276_1_EbH.root",
  sampleBaseDir+"/pat/PATtuple_277_1_Eej.root",
  sampleBaseDir+"/pat/PATtuple_278_1_56a.root",
  sampleBaseDir+"/pat/PATtuple_279_1_PbP.root",
  sampleBaseDir+"/pat/PATtuple_280_1_hgO.root",
  sampleBaseDir+"/pat/PATtuple_281_1_uCd.root",
  sampleBaseDir+"/pat/PATtuple_282_1_Bxh.root",
  sampleBaseDir+"/pat/PATtuple_283_1_TeS.root",
  sampleBaseDir+"/pat/PATtuple_284_1_0z8.root",
  sampleBaseDir+"/pat/PATtuple_285_1_PrV.root",
  sampleBaseDir+"/pat/PATtuple_286_1_WQA.root",
  sampleBaseDir+"/pat/PATtuple_287_1_yMa.root",
  sampleBaseDir+"/pat/PATtuple_288_1_XWm.root",
  sampleBaseDir+"/pat/PATtuple_289_1_eBg.root",
  sampleBaseDir+"/pat/PATtuple_290_1_Zu2.root",
  sampleBaseDir+"/pat/PATtuple_291_1_Vz1.root",
  sampleBaseDir+"/pat/PATtuple_292_1_EEx.root",
  sampleBaseDir+"/pat/PATtuple_293_1_sLt.root",
  sampleBaseDir+"/pat/PATtuple_294_1_Wkf.root",
  sampleBaseDir+"/pat/PATtuple_295_1_5WY.root",
  sampleBaseDir+"/pat/PATtuple_296_1_TYa.root",
  sampleBaseDir+"/pat/PATtuple_297_1_Vg5.root",
  sampleBaseDir+"/pat/PATtuple_298_1_DpW.root",
  sampleBaseDir+"/pat/PATtuple_299_1_xu0.root",
  sampleBaseDir+"/pat/PATtuple_300_1_qLK.root",
  sampleBaseDir+"/pat/PATtuple_301_1_PXW.root",
  sampleBaseDir+"/pat/PATtuple_302_1_QMz.root",
  sampleBaseDir+"/pat/PATtuple_303_1_tEB.root",
  sampleBaseDir+"/pat/PATtuple_304_1_76r.root",
  sampleBaseDir+"/pat/PATtuple_305_1_RXU.root",
  sampleBaseDir+"/pat/PATtuple_306_1_iL6.root",
  sampleBaseDir+"/pat/PATtuple_307_1_tOc.root",
  sampleBaseDir+"/pat/PATtuple_308_1_576.root",
  sampleBaseDir+"/pat/PATtuple_309_1_mBi.root",
  sampleBaseDir+"/pat/PATtuple_310_1_P1D.root",
  sampleBaseDir+"/pat/PATtuple_311_1_rcF.root",
  sampleBaseDir+"/pat/PATtuple_312_1_Awd.root",
  sampleBaseDir+"/pat/PATtuple_313_1_C0R.root",
  sampleBaseDir+"/pat/PATtuple_314_1_GvB.root",
  sampleBaseDir+"/pat/PATtuple_315_1_Usb.root",
  sampleBaseDir+"/pat/PATtuple_316_1_paO.root",
  sampleBaseDir+"/pat/PATtuple_317_1_oRp.root",
  sampleBaseDir+"/pat/PATtuple_318_1_AVf.root",
  sampleBaseDir+"/pat/PATtuple_319_1_eFu.root",
  sampleBaseDir+"/pat/PATtuple_320_1_ZhC.root",
  sampleBaseDir+"/pat/PATtuple_321_1_iqx.root",
  sampleBaseDir+"/pat/PATtuple_322_1_eZO.root",
  sampleBaseDir+"/pat/PATtuple_323_1_1fh.root",
  sampleBaseDir+"/pat/PATtuple_324_1_8lI.root",
  sampleBaseDir+"/pat/PATtuple_325_0_9CU.root",
  sampleBaseDir+"/pat/PATtuple_326_0_0hG.root",
  sampleBaseDir+"/pat/PATtuple_327_0_GbH.root",
  sampleBaseDir+"/pat/PATtuple_328_0_5Ne.root",
  sampleBaseDir+"/pat/PATtuple_329_0_gVw.root",
  sampleBaseDir+"/pat/PATtuple_330_0_NfG.root",
  sampleBaseDir+"/pat/PATtuple_331_0_zgS.root",
  sampleBaseDir+"/pat/PATtuple_332_0_Fd0.root",
  sampleBaseDir+"/pat/PATtuple_333_0_Wn9.root",
  sampleBaseDir+"/pat/PATtuple_334_0_srM.root",
  sampleBaseDir+"/pat/PATtuple_335_0_uRk.root",
  sampleBaseDir+"/pat/PATtuple_336_0_Tgl.root",
  sampleBaseDir+"/pat/PATtuple_337_0_KXh.root",
  sampleBaseDir+"/pat/PATtuple_338_0_0Oz.root",
  sampleBaseDir+"/pat/PATtuple_339_0_BaF.root",
  sampleBaseDir+"/pat/PATtuple_340_0_th1.root",
  sampleBaseDir+"/pat/PATtuple_341_0_ODx.root",
  sampleBaseDir+"/pat/PATtuple_342_0_K06.root",
  sampleBaseDir+"/pat/PATtuple_343_0_gl8.root",
  sampleBaseDir+"/pat/PATtuple_344_0_gqz.root",
  sampleBaseDir+"/pat/PATtuple_345_0_zKs.root",
  sampleBaseDir+"/pat/PATtuple_346_0_sQn.root",
  sampleBaseDir+"/pat/PATtuple_347_0_gWO.root",
  sampleBaseDir+"/pat/PATtuple_348_0_T3F.root",
  sampleBaseDir+"/pat/PATtuple_349_0_mYi.root",
  sampleBaseDir+"/pat/PATtuple_350_0_niJ.root",
  sampleBaseDir+"/pat/PATtuple_351_0_aTY.root",
  sampleBaseDir+"/pat/PATtuple_352_0_98o.root",
  sampleBaseDir+"/pat/PATtuple_353_0_S3B.root",
  sampleBaseDir+"/pat/PATtuple_354_0_Rto.root",
  sampleBaseDir+"/pat/PATtuple_355_0_PXv.root",
  sampleBaseDir+"/pat/PATtuple_356_0_1to.root",
  sampleBaseDir+"/pat/PATtuple_357_0_uUY.root",
  sampleBaseDir+"/pat/PATtuple_358_0_SPZ.root",
  sampleBaseDir+"/pat/PATtuple_359_0_OQo.root",
  sampleBaseDir+"/pat/PATtuple_360_0_Lqq.root",
  sampleBaseDir+"/pat/PATtuple_361_0_E4G.root",
  sampleBaseDir+"/pat/PATtuple_362_0_EJh.root",
  sampleBaseDir+"/pat/PATtuple_363_0_W1C.root",
  sampleBaseDir+"/pat/PATtuple_364_0_bgM.root",
  sampleBaseDir+"/pat/PATtuple_365_0_njk.root",
  sampleBaseDir+"/pat/PATtuple_366_0_p3g.root",
  sampleBaseDir+"/pat/PATtuple_367_0_I1v.root",
  sampleBaseDir+"/pat/PATtuple_368_0_FVq.root",
  sampleBaseDir+"/pat/PATtuple_369_0_nPI.root",
  sampleBaseDir+"/pat/PATtuple_370_0_gdW.root",
  sampleBaseDir+"/pat/PATtuple_371_0_NHn.root",
  sampleBaseDir+"/pat/PATtuple_372_0_vOz.root",
  sampleBaseDir+"/pat/PATtuple_373_0_ew4.root",
  sampleBaseDir+"/pat/PATtuple_374_0_xeq.root",
  sampleBaseDir+"/pat/PATtuple_375_0_zeo.root",
  sampleBaseDir+"/pat/PATtuple_376_0_G32.root",
  sampleBaseDir+"/pat/PATtuple_377_0_9du.root",
  sampleBaseDir+"/pat/PATtuple_378_0_1ho.root",
  sampleBaseDir+"/pat/PATtuple_379_0_Jlg.root",
  sampleBaseDir+"/pat/PATtuple_380_0_gZ8.root",
  sampleBaseDir+"/pat/PATtuple_381_0_bDu.root",
  sampleBaseDir+"/pat/PATtuple_382_0_Yr6.root",
  sampleBaseDir+"/pat/PATtuple_383_0_mMW.root",
  sampleBaseDir+"/pat/PATtuple_384_0_p36.root",
  sampleBaseDir+"/pat/PATtuple_385_0_gUf.root",
  sampleBaseDir+"/pat/PATtuple_386_0_Btp.root",
  sampleBaseDir+"/pat/PATtuple_387_0_cm7.root",
  sampleBaseDir+"/pat/PATtuple_388_0_6Vu.root",
  sampleBaseDir+"/pat/PATtuple_389_0_ZKR.root",
  sampleBaseDir+"/pat/PATtuple_390_0_v0i.root",
  sampleBaseDir+"/pat/PATtuple_391_0_7sh.root",
  sampleBaseDir+"/pat/PATtuple_392_0_yAB.root",
  sampleBaseDir+"/pat/PATtuple_393_0_7Q6.root",
  sampleBaseDir+"/pat/PATtuple_394_0_pDj.root",
  sampleBaseDir+"/pat/PATtuple_395_0_rWT.root",
  sampleBaseDir+"/pat/PATtuple_396_0_WqG.root",
  sampleBaseDir+"/pat/PATtuple_397_0_DcM.root",
  sampleBaseDir+"/pat/PATtuple_398_0_jJA.root",
  sampleBaseDir+"/pat/PATtuple_399_0_9pD.root",
  sampleBaseDir+"/pat/PATtuple_400_0_gKu.root",
  sampleBaseDir+"/pat/PATtuple_401_0_Ldr.root",
  sampleBaseDir+"/pat/PATtuple_402_0_Kwp.root",
  sampleBaseDir+"/pat/PATtuple_403_0_LMG.root",
  sampleBaseDir+"/pat/PATtuple_404_0_zJj.root",
  sampleBaseDir+"/pat/PATtuple_405_0_r1L.root",
  sampleBaseDir+"/pat/PATtuple_406_0_3Au.root",
  sampleBaseDir+"/pat/PATtuple_407_0_S51.root",
  sampleBaseDir+"/pat/PATtuple_408_0_ZRM.root",
  sampleBaseDir+"/pat/PATtuple_409_0_vEN.root",
  sampleBaseDir+"/pat/PATtuple_410_0_Nyh.root",
  sampleBaseDir+"/pat/PATtuple_411_0_p9p.root",
  sampleBaseDir+"/pat/PATtuple_412_0_oS1.root",
  sampleBaseDir+"/pat/PATtuple_413_0_Qsz.root",
  sampleBaseDir+"/pat/PATtuple_414_0_7Ys.root",
  sampleBaseDir+"/pat/PATtuple_415_0_JKv.root",
  sampleBaseDir+"/pat/PATtuple_416_0_KDp.root",
  sampleBaseDir+"/pat/PATtuple_417_0_zZs.root",
  sampleBaseDir+"/pat/PATtuple_418_0_mge.root",
  sampleBaseDir+"/pat/PATtuple_419_0_Bxp.root",
  sampleBaseDir+"/pat/PATtuple_420_0_Dsz.root",
  sampleBaseDir+"/pat/PATtuple_421_0_y6f.root",
  sampleBaseDir+"/pat/PATtuple_422_0_phl.root",
  sampleBaseDir+"/pat/PATtuple_423_0_Ccv.root",
  sampleBaseDir+"/pat/PATtuple_424_0_j8N.root",
  sampleBaseDir+"/pat/PATtuple_425_0_EpO.root",
  sampleBaseDir+"/pat/PATtuple_426_0_Vdz.root",
  sampleBaseDir+"/pat/PATtuple_427_0_Pxd.root",
  sampleBaseDir+"/pat/PATtuple_428_0_inM.root",
  sampleBaseDir+"/pat/PATtuple_429_0_Q0s.root",
  sampleBaseDir+"/pat/PATtuple_430_0_CQF.root",
  sampleBaseDir+"/pat/PATtuple_431_0_kIS.root",
  sampleBaseDir+"/pat/PATtuple_432_0_WeO.root",
  sampleBaseDir+"/pat/PATtuple_433_0_AWR.root",
  sampleBaseDir+"/pat/PATtuple_434_0_dzO.root",
  sampleBaseDir+"/pat/PATtuple_435_0_sgs.root",
  sampleBaseDir+"/pat/PATtuple_436_0_Uia.root",
  sampleBaseDir+"/pat/PATtuple_437_0_Dgb.root",
  sampleBaseDir+"/pat/PATtuple_438_0_mm6.root",
  sampleBaseDir+"/pat/PATtuple_439_0_nJz.root",
  sampleBaseDir+"/pat/PATtuple_440_0_i3d.root",
  sampleBaseDir+"/pat/PATtuple_441_0_TlD.root",
  sampleBaseDir+"/pat/PATtuple_442_0_YCi.root",
  sampleBaseDir+"/pat/PATtuple_443_0_5Cm.root",
  sampleBaseDir+"/pat/PATtuple_444_0_5Sy.root",
  sampleBaseDir+"/pat/PATtuple_445_0_5BG.root",
  sampleBaseDir+"/pat/PATtuple_446_0_maa.root",
  sampleBaseDir+"/pat/PATtuple_447_0_pPJ.root",
  sampleBaseDir+"/pat/PATtuple_448_0_Yr1.root",
  sampleBaseDir+"/pat/PATtuple_449_0_aFN.root",
  sampleBaseDir+"/pat/PATtuple_450_0_1ih.root",
  sampleBaseDir+"/pat/PATtuple_451_0_OBn.root",
  sampleBaseDir+"/pat/PATtuple_452_0_CMw.root",
  sampleBaseDir+"/pat/PATtuple_453_0_mmi.root",
  sampleBaseDir+"/pat/PATtuple_454_0_ntE.root",
  sampleBaseDir+"/pat/PATtuple_455_0_zmF.root",
  sampleBaseDir+"/pat/PATtuple_456_0_Bfm.root",
  sampleBaseDir+"/pat/PATtuple_457_0_N8J.root",
  sampleBaseDir+"/pat/PATtuple_458_0_xKz.root",
  sampleBaseDir+"/pat/PATtuple_459_0_s4d.root",
  sampleBaseDir+"/pat/PATtuple_460_0_iTF.root",
  sampleBaseDir+"/pat/PATtuple_461_0_xz0.root",
  sampleBaseDir+"/pat/PATtuple_462_0_q2p.root",
  sampleBaseDir+"/pat/PATtuple_463_0_B4u.root",
  sampleBaseDir+"/pat/PATtuple_464_0_VIE.root",
  sampleBaseDir+"/pat/PATtuple_465_0_Re5.root",
  sampleBaseDir+"/pat/PATtuple_466_0_UjB.root",
  sampleBaseDir+"/pat/PATtuple_467_0_fQ1.root",
  sampleBaseDir+"/pat/PATtuple_468_0_f5r.root",
  sampleBaseDir+"/pat/PATtuple_469_0_Snv.root",
  sampleBaseDir+"/pat/PATtuple_470_0_3GY.root",
  sampleBaseDir+"/pat/PATtuple_471_0_kdP.root",
  sampleBaseDir+"/pat/PATtuple_472_0_kaC.root",
  sampleBaseDir+"/pat/PATtuple_473_0_cGa.root",
  sampleBaseDir+"/pat/PATtuple_474_0_4gO.root",
  sampleBaseDir+"/pat/PATtuple_475_0_LBi.root",
  sampleBaseDir+"/pat/PATtuple_476_0_8oW.root",
  sampleBaseDir+"/pat/PATtuple_477_0_wkS.root",
  sampleBaseDir+"/pat/PATtuple_478_0_2zn.root",
  sampleBaseDir+"/pat/PATtuple_479_0_d0M.root",
  sampleBaseDir+"/pat/PATtuple_480_0_DZI.root",
  sampleBaseDir+"/pat/PATtuple_481_1_tap.root",
  sampleBaseDir+"/pat/PATtuple_482_1_JXZ.root",
  sampleBaseDir+"/pat/PATtuple_483_1_btM.root",
  sampleBaseDir+"/pat/PATtuple_484_1_o6n.root",
  sampleBaseDir+"/pat/PATtuple_485_1_LdX.root",
  sampleBaseDir+"/pat/PATtuple_486_1_d55.root",
  sampleBaseDir+"/pat/PATtuple_487_1_B8F.root",
  sampleBaseDir+"/pat/PATtuple_488_1_sH4.root",
  sampleBaseDir+"/pat/PATtuple_489_1_baP.root",
  sampleBaseDir+"/pat/PATtuple_490_1_fSx.root",
  sampleBaseDir+"/pat/PATtuple_491_1_fpc.root",
  sampleBaseDir+"/pat/PATtuple_492_1_z9j.root",
  sampleBaseDir+"/pat/PATtuple_493_1_qiz.root",
  sampleBaseDir+"/pat/PATtuple_494_1_oCI.root",
  sampleBaseDir+"/pat/PATtuple_495_1_wNe.root",
  sampleBaseDir+"/pat/PATtuple_496_1_9yA.root",
  sampleBaseDir+"/pat/PATtuple_497_1_4sE.root",
  sampleBaseDir+"/pat/PATtuple_498_1_Thg.root",
  sampleBaseDir+"/pat/PATtuple_499_1_YPX.root",
  sampleBaseDir+"/pat/PATtuple_500_1_rTH.root",
  sampleBaseDir+"/pat/PATtuple_501_1_0hA.root",
  sampleBaseDir+"/pat/PATtuple_502_1_Gvo.root",
  sampleBaseDir+"/pat/PATtuple_503_1_ybC.root",
  sampleBaseDir+"/pat/PATtuple_504_1_Pug.root",
  sampleBaseDir+"/pat/PATtuple_505_1_CFR.root",
  sampleBaseDir+"/pat/PATtuple_506_1_PFW.root",
  sampleBaseDir+"/pat/PATtuple_507_1_Xg9.root",
  sampleBaseDir+"/pat/PATtuple_508_1_03q.root",
  sampleBaseDir+"/pat/PATtuple_509_1_FWY.root",
  sampleBaseDir+"/pat/PATtuple_510_1_DAW.root",
  sampleBaseDir+"/pat/PATtuple_511_1_SZ8.root",
  sampleBaseDir+"/pat/PATtuple_512_1_gVh.root",
  sampleBaseDir+"/pat/PATtuple_513_1_ABy.root",
  sampleBaseDir+"/pat/PATtuple_514_1_JZi.root",
  sampleBaseDir+"/pat/PATtuple_515_1_etp.root",
  sampleBaseDir+"/pat/PATtuple_516_1_FiZ.root",
  sampleBaseDir+"/pat/PATtuple_517_1_Mfk.root",
  sampleBaseDir+"/pat/PATtuple_518_1_sze.root",
  sampleBaseDir+"/pat/PATtuple_519_1_gEu.root",
  sampleBaseDir+"/pat/PATtuple_520_1_Dgz.root",
  sampleBaseDir+"/pat/PATtuple_521_1_dK5.root",
  sampleBaseDir+"/pat/PATtuple_522_1_hJF.root",
  sampleBaseDir+"/pat/PATtuple_523_1_IJ3.root",
  sampleBaseDir+"/pat/PATtuple_524_1_ujO.root",
  sampleBaseDir+"/pat/PATtuple_525_1_7kq.root",
  sampleBaseDir+"/pat/PATtuple_526_1_6wd.root",
  sampleBaseDir+"/pat/PATtuple_527_1_lCn.root",
  sampleBaseDir+"/pat/PATtuple_528_1_QRF.root",
  sampleBaseDir+"/pat/PATtuple_529_1_CBE.root",
  sampleBaseDir+"/pat/PATtuple_530_1_eeq.root",
  sampleBaseDir+"/pat/PATtuple_531_1_c5E.root",
  sampleBaseDir+"/pat/PATtuple_532_1_GuR.root",
  sampleBaseDir+"/pat/PATtuple_533_1_frR.root",
  sampleBaseDir+"/pat/PATtuple_534_1_OP8.root",
  sampleBaseDir+"/pat/PATtuple_535_1_hDN.root",
  sampleBaseDir+"/pat/PATtuple_536_1_tX5.root",
  sampleBaseDir+"/pat/PATtuple_537_1_LpB.root",
  sampleBaseDir+"/pat/PATtuple_538_1_r8z.root",
  sampleBaseDir+"/pat/PATtuple_539_1_e9A.root",
  sampleBaseDir+"/pat/PATtuple_540_1_jCK.root",
  sampleBaseDir+"/pat/PATtuple_541_1_cUb.root",
  sampleBaseDir+"/pat/PATtuple_542_1_pLu.root",
  sampleBaseDir+"/pat/PATtuple_543_1_XHc.root",
  sampleBaseDir+"/pat/PATtuple_544_1_4sZ.root",
  sampleBaseDir+"/pat/PATtuple_545_1_uwa.root",
  sampleBaseDir+"/pat/PATtuple_546_1_2nD.root",
  sampleBaseDir+"/pat/PATtuple_547_1_CXc.root",
  sampleBaseDir+"/pat/PATtuple_548_1_TLX.root",
  sampleBaseDir+"/pat/PATtuple_549_1_gSf.root",
  sampleBaseDir+"/pat/PATtuple_550_1_dDC.root",
  sampleBaseDir+"/pat/PATtuple_551_1_Xgt.root",
  sampleBaseDir+"/pat/PATtuple_552_1_wKu.root",
  sampleBaseDir+"/pat/PATtuple_553_1_Lqg.root",
  sampleBaseDir+"/pat/PATtuple_554_1_rct.root",
  sampleBaseDir+"/pat/PATtuple_555_1_EsC.root",
  sampleBaseDir+"/pat/PATtuple_556_1_j7l.root",
  sampleBaseDir+"/pat/PATtuple_557_1_XHR.root",
  sampleBaseDir+"/pat/PATtuple_558_1_eG2.root",
  sampleBaseDir+"/pat/PATtuple_559_1_qae.root",
  sampleBaseDir+"/pat/PATtuple_560_1_XwK.root",
  sampleBaseDir+"/pat/PATtuple_561_1_b4z.root",
  sampleBaseDir+"/pat/PATtuple_562_1_Fvg.root",
  sampleBaseDir+"/pat/PATtuple_563_1_Sk5.root",
  sampleBaseDir+"/pat/PATtuple_564_1_GOV.root",
  sampleBaseDir+"/pat/PATtuple_565_1_w4c.root",
  sampleBaseDir+"/pat/PATtuple_566_1_Htp.root",
  sampleBaseDir+"/pat/PATtuple_567_1_QjD.root",
  sampleBaseDir+"/pat/PATtuple_568_1_9e7.root",
  sampleBaseDir+"/pat/PATtuple_569_1_c14.root",
  sampleBaseDir+"/pat/PATtuple_570_1_iHK.root",
  sampleBaseDir+"/pat/PATtuple_571_1_UzW.root",
  sampleBaseDir+"/pat/PATtuple_572_1_Mdd.root",
  sampleBaseDir+"/pat/PATtuple_573_1_HBb.root",
  sampleBaseDir+"/pat/PATtuple_574_1_XIj.root",
  sampleBaseDir+"/pat/PATtuple_575_1_Htp.root",
  sampleBaseDir+"/pat/PATtuple_576_1_x7c.root",
  sampleBaseDir+"/pat/PATtuple_577_1_Byr.root",
  sampleBaseDir+"/pat/PATtuple_578_1_Mua.root",
  sampleBaseDir+"/pat/PATtuple_579_1_YvK.root",
  sampleBaseDir+"/pat/PATtuple_580_1_3MI.root",
  sampleBaseDir+"/pat/PATtuple_581_1_6QM.root",
  sampleBaseDir+"/pat/PATtuple_582_1_uOr.root",
  sampleBaseDir+"/pat/PATtuple_583_1_Chc.root",
  sampleBaseDir+"/pat/PATtuple_584_1_vRA.root",
  sampleBaseDir+"/pat/PATtuple_585_1_3xh.root",
  sampleBaseDir+"/pat/PATtuple_586_1_agh.root",
  sampleBaseDir+"/pat/PATtuple_587_1_ZsH.root",
  sampleBaseDir+"/pat/PATtuple_588_1_Kni.root",
  sampleBaseDir+"/pat/PATtuple_589_1_A1H.root",
  sampleBaseDir+"/pat/PATtuple_590_1_uxS.root",
  sampleBaseDir+"/pat/PATtuple_591_1_3NG.root",
  sampleBaseDir+"/pat/PATtuple_592_1_SX0.root",
  sampleBaseDir+"/pat/PATtuple_593_1_mhr.root",
  sampleBaseDir+"/pat/PATtuple_594_1_r0W.root",
  sampleBaseDir+"/pat/PATtuple_595_1_i3c.root",
  sampleBaseDir+"/pat/PATtuple_596_1_kLN.root",
  sampleBaseDir+"/pat/PATtuple_597_1_8ej.root",
  sampleBaseDir+"/pat/PATtuple_598_1_zzQ.root",
  sampleBaseDir+"/pat/PATtuple_599_1_tDg.root",
  sampleBaseDir+"/pat/PATtuple_600_1_hFD.root",
  sampleBaseDir+"/pat/PATtuple_601_1_uzw.root",
  sampleBaseDir+"/pat/PATtuple_602_1_yF4.root",
  sampleBaseDir+"/pat/PATtuple_603_2_Vp2.root",
  sampleBaseDir+"/pat/PATtuple_604_1_qsr.root",
  sampleBaseDir+"/pat/PATtuple_605_1_H0k.root",
  sampleBaseDir+"/pat/PATtuple_606_1_bMf.root",
  sampleBaseDir+"/pat/PATtuple_607_1_xBL.root",
  sampleBaseDir+"/pat/PATtuple_608_1_Qlk.root",
  sampleBaseDir+"/pat/PATtuple_609_1_mCe.root",
  sampleBaseDir+"/pat/PATtuple_610_1_tMz.root",
  sampleBaseDir+"/pat/PATtuple_611_1_4W0.root",
  sampleBaseDir+"/pat/PATtuple_612_1_UEz.root",
  sampleBaseDir+"/pat/PATtuple_613_1_Y7Q.root",
  sampleBaseDir+"/pat/PATtuple_614_1_brb.root",
  sampleBaseDir+"/pat/PATtuple_615_1_YxX.root",
  sampleBaseDir+"/pat/PATtuple_616_1_Kzu.root",
  sampleBaseDir+"/pat/PATtuple_617_1_qzg.root",
  sampleBaseDir+"/pat/PATtuple_618_1_UHg.root",
  sampleBaseDir+"/pat/PATtuple_619_1_Fhz.root",
  sampleBaseDir+"/pat/PATtuple_620_1_fF2.root",
  sampleBaseDir+"/pat/PATtuple_621_1_jtu.root",
  sampleBaseDir+"/pat/PATtuple_622_1_Szy.root",
  sampleBaseDir+"/pat/PATtuple_623_1_Y4l.root",
  sampleBaseDir+"/pat/PATtuple_624_1_scW.root",
  sampleBaseDir+"/pat/PATtuple_625_1_Bld.root",
  sampleBaseDir+"/pat/PATtuple_626_1_bUS.root",
  sampleBaseDir+"/pat/PATtuple_627_1_gZQ.root",
  sampleBaseDir+"/pat/PATtuple_628_1_YZP.root",
  sampleBaseDir+"/pat/PATtuple_629_1_0gm.root",
  sampleBaseDir+"/pat/PATtuple_630_1_gnC.root",
  sampleBaseDir+"/pat/PATtuple_631_1_8Qx.root",
  sampleBaseDir+"/pat/PATtuple_632_1_208.root",
  sampleBaseDir+"/pat/PATtuple_633_1_PE5.root",
  sampleBaseDir+"/pat/PATtuple_634_1_9c3.root",
  sampleBaseDir+"/pat/PATtuple_635_1_y6f.root",
  sampleBaseDir+"/pat/PATtuple_636_1_35K.root",
  sampleBaseDir+"/pat/PATtuple_637_1_4sm.root",
  sampleBaseDir+"/pat/PATtuple_638_1_39v.root",
  sampleBaseDir+"/pat/PATtuple_639_1_Yxv.root",
  sampleBaseDir+"/pat/PATtuple_640_1_flg.root",
  sampleBaseDir+"/pat/PATtuple_641_1_D1x.root",
  sampleBaseDir+"/pat/PATtuple_642_1_afQ.root",
  sampleBaseDir+"/pat/PATtuple_643_1_dAu.root",
  sampleBaseDir+"/pat/PATtuple_644_1_1n0.root",
  sampleBaseDir+"/pat/PATtuple_645_1_dhV.root",
  sampleBaseDir+"/pat/PATtuple_646_1_8Jm.root"
]

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "MC"
sampleRunMu = 0
