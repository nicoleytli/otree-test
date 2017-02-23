from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass

class p1(Page):
    form_model = models.Player
    form_fields = ['attractive_1', 'masculine_1', 'intelligent_1', 'unaggressive_1', 'trustworthy_1', 'confident_1',
                   'loss_1', 'quality_1']

class p2(Page):
    form_model = models.Player
    form_fields = ['attractive_2', 'masculine_2', 'intelligent_2', 'unaggressive_2', 'trustworthy_2', 'confident_2',
                   'loss_2', 'quality_2']

class p3(Page):
    form_model = models.Player
    form_fields = ['attractive_3', 'masculine_3', 'intelligent_3', 'unaggressive_3', 'trustworthy_3', 'confident_3', 'loss_3',
                   'quality_3']

class p4(Page):
    form_model = models.Player
    form_fields = ['attractive_4', 'masculine_4', 'intelligent_4', 'unaggressive_4', 'trustworthy_4', 'confident_4', 'loss_4',
                   'quality_4']

class p5(Page):
    form_model = models.Player
    form_fields = ['attractive_5', 'masculine_5', 'intelligent_5', 'unaggressive_5', 'trustworthy_5', 'confident_5', 'loss_5',
                   'quality_5']

class p6(Page):
    form_model = models.Player
    form_fields = ['attractive_6', 'masculine_6', 'intelligent_6', 'unaggressive_6', 'trustworthy_6', 'confident_6', 'loss_6',
                   'quality_6']

class p7(Page):
    form_model = models.Player
    form_fields = ['attractive_7', 'masculine_7', 'intelligent_7', 'unaggressive_7', 'trustworthy_7', 'confident_7', 'loss_7',
                   'quality_7']

class p8(Page):
    form_model = models.Player
    form_fields = ['attractive_8', 'masculine_8', 'intelligent_8', 'unaggressive_8', 'trustworthy_8', 'confident_8', 'loss_8',
                   'quality_8']

class p9(Page):
    form_model = models.Player
    form_fields = ['attractive', 'masculine', 'intelligent', 'unaggressive', 'trustworthy', 'confident', 'loss',
                   'quality']

class p10(Page):
    form_model = models.Player
    form_fields = ['attractive_9', 'masculine_9', 'intelligent_9', 'unaggressive_9', 'trustworthy_9', 'confident_9', 'loss_9',
                   'quality_9']

class p11(Page):
    form_model = models.Player
    form_fields = ['attractive_10', 'masculine_10', 'intelligent_10', 'unaggressive_10', 'trustworthy_10', 'confident_10', 'loss_10',
                   'quality_10']

class p12(Page):
    form_model = models.Player
    form_fields = ['attractive_11', 'masculine_11', 'intelligent_11', 'unaggressive_11', 'trustworthy_11', 'confident_11', 'loss_11',
                   'quality_11']

class p13(Page):
    form_model = models.Player
    form_fields = ['attractive_12', 'masculine_12', 'intelligent_12', 'unaggressive_12', 'trustworthy_12', 'confident_12', 'loss_12',
                   'quality_12']

class p14(Page):
    form_model = models.Player
    form_fields = ['attractive_13', 'masculine_13', 'intelligent_13', 'unaggressive_13', 'trustworthy_13', 'confident_13', 'loss_13',
                   'quality_13']

class p15(Page):
    form_model = models.Player
    form_fields = ['attractive_14', 'masculine_14', 'intelligent_14', 'unaggressive_14', 'trustworthy_14', 'confident_14', 'loss_14',
                   'quality_14']

class p16(Page):
    form_model = models.Player
    form_fields = ['attractive_15', 'masculine_15', 'intelligent_15', 'unaggressive_15', 'trustworthy_15', 'confident_15', 'loss_15',
                   'quality_15']

class p17(Page):
    form_model = models.Player
    form_fields = ['attractive_16', 'masculine_16', 'intelligent_16', 'unaggressive_16', 'trustworthy_16', 'confident_16', 'loss_16',
                   'quality_16']

class p18(Page):
    form_model = models.Player
    form_fields = ['attractive_17', 'masculine_17', 'intelligent_17', 'unaggressive_17', 'trustworthy_17', 'confident_17', 'loss_17',
                   'quality_17']

class p19(Page):
    form_model = models.Player
    form_fields = ['attractive_18', 'masculine_18', 'intelligent_18', 'unaggressive_18', 'trustworthy_18', 'confident_18', 'loss_18',
                   'quality_18']

class p20(Page):
    form_model = models.Player
    form_fields = ['attractive_19', 'masculine_19', 'intelligent_19', 'unaggressive_19', 'trustworthy_19', 'confident_19', 'loss_19',
                   'quality_19']

class p21(Page):
    form_model = models.Player
    form_fields = ['attractive_20', 'masculine_20', 'intelligent_20', 'unaggressive_20', 'trustworthy_20', 'confident_20', 'loss_20',
                   'quality_20']

class p22(Page):
    form_model = models.Player
    form_fields = ['attractive_21', 'masculine_21', 'intelligent_21', 'unaggressive_21', 'trustworthy_21', 'confident_21', 'loss_21',
                   'quality_21']

class p23(Page):
    form_model = models.Player
    form_fields = ['attractive_22', 'masculine_22', 'intelligent_22', 'unaggressive_22', 'trustworthy_22', 'confident_22', 'loss_22',
                   'quality_22']

class p24(Page):
    form_model = models.Player
    form_fields = ['attractive_23', 'masculine_23', 'intelligent_23', 'unaggressive_23', 'trustworthy_23', 'confident_23', 'loss_23',
                   'quality_23']

class p25(Page):
    form_model = models.Player
    form_fields = ['attractive_24', 'masculine_24', 'intelligent_24', 'unaggressive_24', 'trustworthy_24', 'confident_24', 'loss_24',
                   'quality_24']

class p26(Page):
    form_model = models.Player
    form_fields = ['attractive_25', 'masculine_25', 'intelligent_25', 'unaggressive_25', 'trustworthy_25', 'confident_25', 'loss_25',
                   'quality_25']

class p27(Page):
    form_model = models.Player
    form_fields = ['attractive_26', 'masculine_26', 'intelligent_26', 'unaggressive_26', 'trustworthy_26', 'confident_26', 'loss_26',
                   'quality_26']

class p28(Page):
    form_model = models.Player
    form_fields = ['attractive_27', 'masculine_27', 'intelligent_27', 'unaggressive_27', 'trustworthy_27', 'confident_27', 'loss_27',
                   'quality_27']

class p29(Page):
    form_model = models.Player
    form_fields = ['attractive_28', 'masculine_28', 'intelligent_28', 'unaggressive_28', 'trustworthy_28', 'confident_28', 'loss_28',
                   'quality_28']

class p30(Page):
    form_model = models.Player
    form_fields = ['attractive_29', 'masculine_29', 'intelligent_29', 'unaggressive_29', 'trustworthy_29', 'confident_29', 'loss_29',
                   'quality_29']

class p31(Page):
    form_model = models.Player
    form_fields = ['attractive_30', 'masculine_30', 'intelligent_30', 'unaggressive_30', 'trustworthy_30', 'confident_30', 'loss_30',
                   'quality_30']

class p32(Page):
    form_model = models.Player
    form_fields = ['attractive_31', 'masculine_31', 'intelligent_31', 'unaggressive_31', 'trustworthy_31', 'confident_31', 'loss_31',
                   'quality_31']

class p33(Page):
    form_model = models.Player
    form_fields = ['attractive_32', 'masculine_32', 'intelligent_32', 'unaggressive_32', 'trustworthy_32', 'confident_32', 'loss_32',
                   'quality_32']

class p34(Page):
    form_model = models.Player
    form_fields = ['attractive_33', 'masculine_33', 'intelligent_33', 'unaggressive_33', 'trustworthy_33', 'confident_33', 'loss_33',
                   'quality_33']

class p35(Page):
    form_model = models.Player
    form_fields = ['attractive_34', 'masculine_34', 'intelligent_34', 'unaggressive_34', 'trustworthy_34', 'confident_34', 'loss_34',
                   'quality_34']

class p36(Page):
    form_model = models.Player
    form_fields = ['attractive_35', 'masculine_35', 'intelligent_35', 'unaggressive_35', 'trustworthy_35', 'confident_35', 'loss_35',
                   'quality_35']

class p37(Page):
    form_model = models.Player
    form_fields = ['attractive_36', 'masculine_36', 'intelligent_36', 'unaggressive_36', 'trustworthy_36', 'confident_36', 'loss_36',
                   'quality_36']

class p38(Page):
    form_model = models.Player
    form_fields = ['attractive_37', 'masculine_37', 'intelligent_37', 'unaggressive_37', 'trustworthy_37', 'confident_37', 'loss_37',
                   'quality_37']

class p39(Page):
    form_model = models.Player
    form_fields = ['attractive_38', 'masculine_38', 'intelligent_38', 'unaggressive_38', 'trustworthy_38', 'confident_38', 'loss_38',
                   'quality_38']

class p40(Page):
    form_model = models.Player
    form_fields = ['attractive_39', 'masculine_39', 'intelligent_39', 'unaggressive_39', 'trustworthy_39', 'confident_39', 'loss_39',
                   'quality_39']

class p41(Page):
    form_model = models.Player
    form_fields = ['attractive_40', 'masculine_40', 'intelligent_40', 'unaggressive_40', 'trustworthy_40', 'confident_40', 'loss_40',
                   'quality_40']

class p42(Page):
    form_model = models.Player
    form_fields = ['attractive_41', 'masculine_41', 'intelligent_41', 'unaggressive_41', 'trustworthy_41', 'confident_41', 'loss_41',
                   'quality_41']

class p43(Page):
    form_model = models.Player
    form_fields = ['attractive_42', 'masculine_42', 'intelligent_42', 'unaggressive_42', 'trustworthy_42', 'confident_42', 'loss_42',
                   'quality_42']

class p44(Page):
    form_model = models.Player
    form_fields = ['attractive_43', 'masculine_43', 'intelligent_43', 'unaggressive_43', 'trustworthy_43', 'confident_43', 'loss_43',
                   'quality_43']

class p45(Page):
    form_model = models.Player
    form_fields = ['attractive_44', 'masculine_44', 'intelligent_44', 'unaggressive_44', 'trustworthy_44', 'confident_44', 'loss_44',
                   'quality_44']

class p46(Page):
    form_model = models.Player
    form_fields = ['attractive_45', 'masculine_45', 'intelligent_45', 'unaggressive_45', 'trustworthy_45', 'confident_45', 'loss_45',
                   'quality_45']

class p47(Page):
    form_model = models.Player
    form_fields = ['attractive_46', 'masculine_46', 'intelligent_46', 'unaggressive_46', 'trustworthy_46', 'confident_46', 'loss_46',
                   'quality_46']

class p48(Page):
    form_model = models.Player
    form_fields = ['attractive_47', 'masculine_47', 'intelligent_47', 'unaggressive_47', 'trustworthy_47', 'confident_47', 'loss_47',
                   'quality_47']

class p49(Page):
    form_model = models.Player
    form_fields = ['attractive_48', 'masculine_48', 'intelligent_48', 'unaggressive_48', 'trustworthy_48', 'confident_48', 'loss_48',
                   'quality_48']

class p50(Page):
    form_model = models.Player
    form_fields = ['attractive_49', 'masculine_49', 'intelligent_49', 'unaggressive_49', 'trustworthy_49', 'confident_49', 'loss_49',
                   'quality_49']

class p51(Page):
    form_model = models.Player
    form_fields = ['attractive_50', 'masculine_50', 'intelligent_50', 'unaggressive_50', 'trustworthy_50', 'confident_50', 'loss_50',
                   'quality_50']

class p52(Page):
    form_model = models.Player
    form_fields = ['attractive_51', 'masculine_51', 'intelligent_51', 'unaggressive_51', 'trustworthy_51', 'confident_51', 'loss_51',
                   'quality_51']

class p53(Page):
    form_model = models.Player
    form_fields = ['attractive_52', 'masculine_52', 'intelligent_52', 'unaggressive_52', 'trustworthy_52', 'confident_52', 'loss_52',
                   'quality_52']

class p54(Page):
    form_model = models.Player
    form_fields = ['attractive_53', 'masculine_53', 'intelligent_53', 'unaggressive_53', 'trustworthy_53', 'confident_53', 'loss_53',
                   'quality_53']

class p55(Page):
    form_model = models.Player
    form_fields = ['attractive_54', 'masculine_54', 'intelligent_54', 'unaggressive_54', 'trustworthy_54', 'confident_54', 'loss_54',
                   'quality_54']

class p56(Page):
    form_model = models.Player
    form_fields = ['attractive_55', 'masculine_55', 'intelligent_55', 'unaggressive_55', 'trustworthy_55', 'confident_55', 'loss_55',
                   'quality_55']

class p57(Page):
    form_model = models.Player
    form_fields = ['attractive_56', 'masculine_56', 'intelligent_56', 'unaggressive_56', 'trustworthy_56', 'confident_56', 'loss_56',
                   'quality_56']

class p58(Page):
    form_model = models.Player
    form_fields = ['attractive_57', 'masculine_57', 'intelligent_57', 'unaggressive_57', 'trustworthy_57', 'confident_57', 'loss_57',
                   'quality_57']

class p59(Page):
    form_model = models.Player
    form_fields = ['attractive_58', 'masculine_58', 'intelligent_58', 'unaggressive_58', 'trustworthy_58', 'confident_58', 'loss_58',
                   'quality_58']

class p60(Page):
    form_model = models.Player
    form_fields = ['attractive_59', 'masculine_59', 'intelligent_59', 'unaggressive_59', 'trustworthy_59', 'confident_59', 'loss_59',
                   'quality_59']

class p61(Page):
    form_model = models.Player
    form_fields = ['attractive_60', 'masculine_60', 'intelligent_60', 'unaggressive_60', 'trustworthy_60', 'confident_60', 'loss_60',
                   'quality_60']

class p62(Page):
    form_model = models.Player
    form_fields = ['attractive_61', 'masculine_61', 'intelligent_61', 'unaggressive_61', 'trustworthy_61', 'confident_61', 'loss_61',
                   'quality_61']

class p63(Page):
    form_model = models.Player
    form_fields = ['attractive_62', 'masculine_62', 'intelligent_62', 'unaggressive_62', 'trustworthy_62', 'confident_62', 'loss_62',
                   'quality_62']

class p64(Page):
    form_model = models.Player
    form_fields = ['attractive_63', 'masculine_63', 'intelligent_63', 'unaggressive_63', 'trustworthy_63', 'confident_63', 'loss_63',
                   'quality_63']

class p45(Page):
    form_model = models.Player
    form_fields = ['attractive_64', 'masculine_64', 'intelligent_64', 'unaggressive_64', 'trustworthy_64', 'confident_64', 'loss_64',
                   'quality_64']

class p65(Page):
    form_model = models.Player
    form_fields = ['attractive_65', 'masculine_65', 'intelligent_65', 'unaggressive_65', 'trustworthy_65', 'confident_65', 'loss_65',
                   'quality_65']

class p66(Page):
    form_model = models.Player
    form_fields = ['attractive_66', 'masculine_66', 'intelligent_66', 'unaggressive_66', 'trustworthy_66', 'confident_66', 'loss_66',
                   'quality_66']

class Demographic(Page):
    form_model = models.Player
    form_fields = ['birth', 'gender', 'state', 'education', 'race', 'income']

page_sequence = [
    p1,
    p2,
    p3,
    p4,
    p5,
    p6,
    p7,
    p8,
    p9,
    p10,
    p11,
    p12,
    p13,
    p14,
    p15,
    p16,
    p17,
    p18,
    p19,
    p20,
    p21,
    p22,
    p23,
    p24,
    p25,
    p26,
    p27,
    p28,
    p29,
    p30,
    p31,
    p32,
    p33,
    p34,
    p35,
    p36,
    p37,
    p38,
    p39,
    p40,
    p41,
    p42,
    p43,
    p44,
    p45,
    p46,
    p47,
    p48,
    p49,
    p50,
    p51,
    p52,
    p53,
    p54,
    p55,
    p56,
    p57,
    p58,
    p59,
    p60,
    p61,
    p62,
    p63,
    p64,
    p65,
    p66,
    Demographic,
    # ResultsWaitPage,
    Results
]
