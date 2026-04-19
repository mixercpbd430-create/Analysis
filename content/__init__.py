"""
Content package - Quản lý nội dung 42 phương pháp phân tích
"""

from content.method01_bottleneck import method as m01
from content.method02_bottleneck_loss import method as m02
from content.method03_ce_analysis import method as m03
from content.method04_fmea import method as m04
from content.method05_fta import method as m05
from content.method06_failure import method as m06
from content.method07_function_tree import method as m07
from content.method08_gap import method as m08
from content.method09_hazop import method as m09
from content.method10_jsa import method as m10
from content.method11_pm import method as m11
from content.method12_ppa_past import method as m12
from content.method13_ppa_process import method as m13
from content.method14_risk import method as m14
from content.method15_trend import method as m15
from content.method16_va import method as m16
from content.method17_wwbla import method as m17
from content.method18_why_why import method as m18
from content.method19_3gen import method as m19
from content.method20_5w_image import method as m20
from content.method21_epmd import method as m21
from content.method22_smed import method as m22
from content.method23_oee import method as m23
from content.method24_16losses import method as m24
from content.method25_pareto import method as m25
from content.method26_spc import method as m26
from content.method27_capacity import method as m27
from content.method28_material_balance import method as m28
from content.method29_msa import method as m29
from content.method30_doe import method as m30
from content.method31_regression import method as m31
from content.method32_vsm import method as m32
from content.method33_pdca import method as m33
from content.method34_kaizen import method as m34
from content.method35_3m import method as m35
from content.method36_energy import method as m36
from content.method37_cba import method as m37
from content.method38_abc import method as m38
from content.method39_mikagami import method as m39
from content.method40_swot import method as m40
from content.method41_rcm import method as m41
from content.method42_mtbf_mttr import method as m42

ALL_METHODS = [m01, m02, m03, m04, m05, m06, m07, m08, m09,
               m10, m11, m12, m13, m14, m15, m16, m17, m18,
               m19, m20, m21, m22, m23, m24, m25, m26, m27,
               m28, m29, m30, m31, m32, m33, m34, m35, m36,
               m37, m38, m39, m40, m41, m42]


PILLAR_INFO = {
    "Focus Improvement": {
        "icon": "🎯",
        "color": "#f97316",
        "description": "Cải tiến trọng điểm - Tập trung giải quyết các tổn thất lớn nhất"
    },
    "Early Management": {
        "icon": "🚀",
        "color": "#8b5cf6",
        "description": "Quản lý sớm - Áp dụng kiến thức từ giai đoạn thiết kế"
    },
    "Planned Maintenance": {
        "icon": "🔧",
        "color": "#3b82f6",
        "description": "Bảo trì có kế hoạch - Duy trì hiệu suất thiết bị tối ưu"
    },
    "Overview": {
        "icon": "📊",
        "color": "#10b981",
        "description": "Tổng quan - Các phương pháp phân tích đa dụng"
    },
    "SHE": {
        "icon": "🛡️",
        "color": "#ef4444",
        "description": "An toàn, Sức khỏe & Môi trường"
    }
}


def get_all_methods():
    """Trả về danh sách tất cả phương pháp (thông tin tóm tắt)"""
    return [
        {
            "id": m["id"],
            "title": m["title"],
            "short_name": m["short_name"],
            "icon": m["icon"],
            "pillar": m["pillar"],
            "description": m["description"]
        }
        for m in ALL_METHODS
    ]


def get_method(method_id):
    """Trả về nội dung đầy đủ của 1 phương pháp"""
    for m in ALL_METHODS:
        if m["id"] == method_id:
            return m
    return None


def get_pillars():
    """Trả về thông tin các pillar"""
    return PILLAR_INFO


def get_methods_by_pillar(pillar_name):
    """Trả về danh sách phương pháp theo pillar"""
    return [m for m in ALL_METHODS if m["pillar"] == pillar_name]
