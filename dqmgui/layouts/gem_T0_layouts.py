def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)

_GEM_OFF_TWIKI = '<a href="https://twiki.cern.ch/twiki/bin/view/CMS/GEMPPDOfflineDQM">Link to TWiki</a>'

###############################################################################
# Summary Map
###############################################################################
GEMLayout(dqmitems, '00 Summary Map',
          [{'path': 'GEM/EventInfo/reportSummaryMap',
            'description': _GEM_OFF_TWIKI}])

###############################################################################
# RecHit Occupancy
###############################################################################
GEMLayout(dqmitems, '01 GE11-M-L1 RecHit Occupancy',
          [{'path': 'GEM/RecHits/occ_xy_GE11-M-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '02 GE11-M-L2 RecHit Occupancy',
          [{'path': 'GEM/RecHits/occ_xy_GE11-M-L2',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '03 GE11-P-L1 RecHit Occupancy',
          [{'path': 'GEM/RecHits/occ_xy_GE11-P-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '04 GE11-P-L2 RecHit Occupancy',
          [{'path': 'GEM/RecHits/occ_xy_GE11-P-L2',
            'description': _GEM_OFF_TWIKI}])

###############################################################################
# RecHit Average Cluster Size
###############################################################################
GEMLayout(dqmitems, '05 GE11-M-L1 RecHit Average Cluster Size',
          [{'path': 'GEM/RecHits/rechit_average_GE11-M-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '06 GE11-M-L2 RecHit Average Cluster Size',
          [{'path': 'GEM/RecHits/rechit_average_GE11-M-L2',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '07 GE11-P-L1 RecHit Average Cluster Size',
          [{'path': 'GEM/RecHits/rechit_average_GE11-P-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '08 GE11-P-L2 RecHit Average Cluster Size',
          [{'path': 'GEM/RecHits/rechit_average_GE11-P-L2',
            'description': _GEM_OFF_TWIKI}])

###############################################################################
# Efficiency
###############################################################################
GEMLayout(dqmitems, '09 GE11-M-L1 Chamber Efficiency',
          [{'path': 'GEM/Efficiency/muonSTA/eff_chamber_GE11-M-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '10 GE11-M-L2 Chamber Efficiency',
          [{'path': 'GEM/Efficiency/muonSTA/eff_chamber_GE11-M-L2',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '11 GE11-P-L1 Chamber Efficiency',
          [{'path': 'GEM/Efficiency/muonSTA/eff_chamber_GE11-P-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '12 GE11-P-L2 Chamber Efficiency',
          [{'path': 'GEM/Efficiency/muonSTA/eff_chamber_GE11-P-L2',
            'description': _GEM_OFF_TWIKI}])

###############################################################################
# Misc
###############################################################################
GEMLayout(dqmitems, '13 GE21-P-L2 DIGI Occupancy',
          [{'path': 'GEM/Digis/occ_GE21-P-L2',
            'description': _GEM_OFF_TWIKI}])


GEMLayout(dqmitems, '14 GEM_chamberEff_chamber_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_chamber_1D', 'description': 'Chamber efficiency'}], 
    )

GEMLayout(dqmitems, '15 GEM_chamberEff_pt_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_pt_1D', 'description': 'pt efficiency'}], 
    )

GEMLayout(dqmitems, '16 GEM_chamberEff_eta_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_eta_1D', 'description': 'eta efficiency'}], 
    )

GEMLayout(dqmitems, '17 GEM_chamberEff_phi_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_phi_1D', 'description': 'phi efficiency'}], 
    )

GEMLayout(dqmitems, '18 GEM_chamberEff_chamber_p1_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_chamber_p1_1D', 'description': 'Chamber p1 efficiency'}], 
    )

GEMLayout(dqmitems, '19 GEM_chamberEff_chamber_p2_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_chamber_p2_1D', 'description': 'Chamber p2 efficiency'}], 
    )

GEMLayout(dqmitems, '20 GEM_chamberEff_chamber_n1_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_chamber_n1_1D', 'description': 'Chamber n1 efficiency'}], 
    )

GEMLayout(dqmitems, '21 GEM_chamberEff_chamber_n2_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_chamber_n2_1D', 'description': 'Chamber n2 efficiency'}], 
    )

GEMLayout(dqmitems, '22 GEM_chamberEff_pt_p1_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_pt_p1_1D', 'description': 'pt p1 efficiency'}], 
    )

GEMLayout(dqmitems, '23 GEM_chamberEff_pt_p2_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_pt_p2_1D', 'description': 'pt p2 efficiency'}], 
    )

GEMLayout(dqmitems, '24 GEM_chamberEff_pt_n1_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_pt_n1_1D', 'description': 'pt n1 efficiency'}], 
    )

GEMLayout(dqmitems, '25 GEM_chamberEff_pt_n2_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_pt_n2_1D', 'description': 'pt n2 efficiency'}], 
    )

GEMLayout(dqmitems, '26 GEM_chamberEff_eta_p1_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_eta_p1_1D', 'description': 'eta p1 efficiency'}], 
    )

GEMLayout(dqmitems, '27 GEM_chamberEff_eta_p2_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_eta_p2_1D', 'description': 'eta p2 efficiency'}], 
    )

GEMLayout(dqmitems, '28 GEM_chamberEff_eta_n1_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_eta_n1_1D', 'description': 'eta n1 efficiency'}], 
    )

GEMLayout(dqmitems, '29 GEM_chamberEff_eta_n2_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_eta_n2_1D', 'description': 'eta n2 efficiency'}], 
    )

GEMLayout(dqmitems, '30 GEM_chamberEff_phi_p1_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_phi_p1_1D', 'description': 'phi p1 efficiency'}], 
    )

GEMLayout(dqmitems, '31 GEM_chamberEff_phi_p2_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_phi_p2_1D', 'description': 'phi p2 efficiency'}], 
    )

GEMLayout(dqmitems, '32 GEM_chamberEff_phi_n1_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_phi_n1_1D', 'description': 'phi n1 efficiency'}], 
    )

GEMLayout(dqmitems, '33 GEM_chamberEff_phi_n2_1D', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_phi_n2_1D', 'description': 'phi n2 efficiency'}], 
    )

GEMLayout(dqmitems, '34 GEM_chamberEff_Ch_region_GE1', 
    [{'path': 'GEM/Run summary/Segment_TnP/Task/GEM_chamberEff_Ch_region_GE1', 'description': 'chamber VS region efficiency'}], 
    )
