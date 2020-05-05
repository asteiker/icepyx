import pytest
import warnings
import datetime as dt
from shapely.geometry import Polygon

import icepyx.core.APIformatting as apifmt


#DevNote: is this a situation where you'd ideally build a test class, since you're just repeating the
#test function with different inputs? Especially for the _fmt_spaital, where there's >2 tests?

#CMR temporal and spatial formats --> what's the best way to compare formatted text? character by character comparison of strings?

########## _fmt_temporal ##########
def test_time_fmt():
    obs = apifmt._fmt_temporal(dt.datetime(2019,1,11,12,30,30), dt.datetime(2020,10,31,1,15), 'time')
    exp = {'time': '2019-01-11T12:30:30,2020-10-31T01:15:00'}
    assert obs == exp

def test_temporal_fmt():
    obs = apifmt._fmt_temporal(dt.datetime(2019,1,11,12,30,30), dt.datetime(2020,10,31,1,15), 'temporal')
    exp = {'temporal': '2019-01-11T12:30:30Z,2020-10-31T01:15:00Z'}
    assert obs == exp


########## _fmt_spatial ##########
def test_bounding_box_fmt():
    obs = apifmt._fmt_spatial('bounding_box', [-55, 68, -48, 71])
    exp = {'bounding_box': '-55,68,-48,71'}
    assert obs == exp

def test_bbox_fmt():
    obs = apifmt._fmt_spatial('bbox', [-55, 68, -48, 71])
    exp = {'bbox': '-55,68,-48,71'}
    assert obs == exp

def test_polygon_fmt():
    poly = Polygon([[-86.622742, -74.908126, 0.0], [-86.602149, -74.998483, 0.0], [-86.671945, -74.999545, 0.0], [-86.667881, -75.01762, 0.0], [-86.737771, -75.018662, 0.0], [-86.717729, -75.109052, 0.0], [-86.788057, -75.110077, 0.0], [-86.780144, -75.14624, 0.0], [-86.850654, -75.147247, 0.0], [-86.835058, -75.219586, 0.0], [-86.905925, -75.220574, 0.0], [-86.894389, -75.274839, 0.0], [-86.965529, -75.27581, 0.0], [-86.950368, -75.348177, 0.0], [-87.021872, -75.349129, 0.0], [-87.003154, -75.439609, 0.0], [-87.075115, -75.440545, 0.0], [-87.052886, -75.549149, 0.0], [-86.98038, -75.548205, 0.0], [-86.965004, -75.620616, 0.0], [-87.037878, -75.621564, 0.0], [-87.034102, -75.63967, 0.0], [-86.961136, -75.63872, 0.0], [-86.957257, -75.656825, 0.0], [-86.884208, -75.655851, 0.0], [-86.872234, -75.710165, 0.0], [-86.945563, -75.711143, 0.0], [-86.925871, -75.801686, 0.0], [-86.999681, -75.802647, 0.0], [-86.988029, -75.856983, 0.0], [-87.062135, -75.857925, 0.0], [-87.058326, -75.87604, 0.0], [-87.132537, -75.876959, 0.0], [-87.128815, -75.895075, 0.0], [-87.203132, -75.895972, 0.0], [-87.199496, -75.914091, 0.0], [-87.273919, -75.914965, 0.0], [-87.27037, -75.933086, 0.0], [-87.344899, -75.933938, 0.0], [-87.341438, -75.95206, 0.0], [-87.490715, -75.953695, 0.0], [-87.487439, -75.97182, 0.0], [-87.562188, -75.972604, 0.0], [-87.559001, -75.99073, 0.0], [-87.633856, -75.991491, 0.0], [-87.627653, -76.027748, 0.0], [-87.777778, -76.029203, 0.0], [-87.774861, -76.047334, 0.0], [-87.925213, -76.048696, 0.0], [-87.922485, -76.06683, 0.0], [-87.997771, -76.067476, 0.0], [-87.995135, -76.085611, 0.0], [-88.070527, -76.086234, 0.0], [-88.067983, -76.104371, 0.0], [-88.143481, -76.104971, 0.0], [-88.14103, -76.123109, 0.0], [-88.216633, -76.123686, 0.0], [-88.214276, -76.141826, 0.0], [-88.365701, -76.142909, 0.0], [-88.363537, -76.161051, 0.0], [-88.439359, -76.161557, 0.0], [-88.43729, -76.1797, 0.0], [-88.513217, -76.180183, 0.0], [-88.511244, -76.198328, 0.0], [-88.587276, -76.198787, 0.0], [-88.585399, -76.216933, 0.0], [-88.737681, -76.217781, 0.0], [-88.736001, -76.235929, 0.0], [-88.81225, -76.236317, 0.0], [-88.810667, -76.254466, 0.0], [-88.887022, -76.254831, 0.0], [-88.885537, -76.272981, 0.0], [-88.961998, -76.273321, 0.0], [-88.960611, -76.291473, 0.0], [-89.037177, -76.29179, 0.0], [-89.035889, -76.309942, 0.0], [-89.112561, -76.310235, 0.0], [-89.111372, -76.328389, 0.0], [-89.264932, -76.328903, 0.0], [-89.263946, -76.347058, 0.0], [-89.340833, -76.347279, 0.0], [-89.339947, -76.365434, 0.0], [-89.41694, -76.365631, 0.0], [-89.416155, -76.383788, 0.0], [-89.493254, -76.383961, 0.0], [-89.492571, -76.402118, 0.0], [-89.569775, -76.402267, 0.0], [-89.569195, -76.420425, 0.0], [-89.723816, -76.420649, 0.0], [-89.723443, -76.438808, 0.0], [-89.800859, -76.438884, 0.0], [-89.80059, -76.457044, 0.0], [-89.878112, -76.457095, 0.0], [-89.877947, -76.475255, 0.0], [-89.955575, -76.475282, 0.0], [-89.955514, -76.493443, 0.0], [-90.033248, -76.493445, 0.0], [-90.033293, -76.511607, 0.0], [-90.111131, -76.511584, 0.0], [-90.111283, -76.529747, 0.0], [-90.345113, -76.52953, 0.0], [-90.345583, -76.547693, 0.0], [-90.42363, -76.547571, 0.0], [-90.424208, -76.565734, 0.0], [-90.50236, -76.565588, 0.0], [-90.503734, -76.601916, 0.0], [-90.582098, -76.601744, 0.0], [-90.583695, -76.638075, 0.0], [-90.662272, -76.637877, 0.0], [-90.664093, -76.67421, 0.0], [-90.742884, -76.673987, 0.0], [-90.743907, -76.692154, 0.0], [-90.822803, -76.691906, 0.0], [-90.823937, -76.710073, 0.0], [-91.060932, -76.709176, 0.0], [-91.062397, -76.727343, 0.0], [-91.536922, -76.72487, 0.0], [-91.539047, -76.743034, 0.0], [-91.697397, -76.742008, 0.0], [-91.699746, -76.760171, 0.0], [-91.779021, -76.759619, 0.0], [-91.783959, -76.795946, 0.0], [-91.863446, -76.795367, 0.0], [-91.873848, -76.868024, 0.0], [-91.793917, -76.868605, 0.0], [-91.796424, -76.886772, 0.0], [-91.716375, -76.887329, 0.0], [-91.721186, -76.923666, 0.0], [-91.640906, -76.924199, 0.0], [-91.647835, -76.97871, 0.0], [-91.325297, -76.980597, 0.0], [-91.327166, -76.998771, 0.0], [-91.165637, -76.999562, 0.0], [-91.167283, -77.017738, 0.0], [-91.086397, -77.018096, 0.0], [-91.089474, -77.054451, 0.0], [-91.008355, -77.054784, 0.0], [-91.015545, -77.145686, 0.0], [-91.178934, -77.144989, 0.0], [-91.180618, -77.16317, 0.0], [-91.426015, -77.16193, 0.0], [-91.434206, -77.234653, 0.0], [-92.092069, -77.230176, 0.0], [-92.08907, -77.212001, 0.0], [-92.335283, -77.209895, 0.0], [-92.352136, -77.300761, 0.0], [-92.269483, -77.301495, 0.0], [-92.276054, -77.337847, 0.0], [-92.193152, -77.338557, 0.0], [-92.199521, -77.374914, 0.0], [-92.282662, -77.374202, 0.0], [-92.285981, -77.392381, 0.0], [-92.369233, -77.391642, 0.0], [-92.383091, -77.464357, 0.0], [-92.466819, -77.463587, 0.0], [-92.470431, -77.481766, 0.0], [-92.386581, -77.482537, 0.0], [-92.390081, -77.500717, 0.0], [-92.138102, -77.502874, 0.0], [-92.141243, -77.521058, 0.0], [-91.972963, -77.522365, 0.0], [-91.984627, -77.595116, 0.0], [-91.899978, -77.595733, 0.0], [-91.90279, -77.613923, 0.0], [-91.4788, -77.616608, 0.0], [-91.480993, -77.634803, 0.0], [-91.14118, -77.636469, 0.0], [-91.14799, -77.709264, 0.0], [-91.062516, -77.709615, 0.0], [-91.070502, -77.800626, 0.0], [-90.812128, -77.801523, 0.0], [-90.81335, -77.819728, 0.0], [-90.727088, -77.819973, 0.0], [-90.732603, -77.911009, 0.0], [-90.81952, -77.910763, 0.0], [-90.820765, -77.928971, 0.0], [-90.90781, -77.928697, 0.0], [-90.909191, -77.946905, 0.0], [-90.822014, -77.94718, 0.0], [-90.823267, -77.96539, 0.0], [-90.735953, -77.965638, 0.0], [-90.737076, -77.983849, 0.0], [-90.824523, -77.983601, 0.0], [-90.825784, -78.001812, 0.0], [-90.91336, -78.001535, 0.0], [-90.914759, -78.019746, 0.0], [-91.090167, -78.019109, 0.0], [-91.093515, -78.055531, 0.0], [-91.181481, -78.05517, 0.0], [-91.188783, -78.128018, 0.0], [-91.365784, -78.127206, 0.0], [-91.370017, -78.163631, 0.0], [-91.458782, -78.163181, 0.0], [-91.463317, -78.199607, 0.0], [-91.552351, -78.199128, 0.0], [-91.554767, -78.217341, 0.0], [-91.643932, -78.216832, 0.0], [-91.651645, -78.271472, 0.0], [-91.830785, -78.270365, 0.0], [-91.833652, -78.288578, 0.0], [-92.013037, -78.287355, 0.0], [-92.016194, -78.305566, 0.0], [-92.106013, -78.30491, 0.0], [-92.115968, -78.359544, 0.0], [-92.025726, -78.360203, 0.0], [-92.035347, -78.414844, 0.0], [-91.944667, -78.415477, 0.0], [-91.947751, -78.433693, 0.0], [-91.856918, -78.434298, 0.0], [-91.859867, -78.452516, 0.0], [-91.76888, -78.453093, 0.0], [-91.771695, -78.471312, 0.0], [-91.680555, -78.471861, 0.0], [-91.683233, -78.490081, 0.0], [-91.591939, -78.490602, 0.0], [-91.59703, -78.527046, 0.0], [-91.505436, -78.52754, 0.0], [-91.507847, -78.545764, 0.0], [-91.324343, -78.546665, 0.0], [-91.330738, -78.601343, 0.0], [-91.238533, -78.601752, 0.0], [-91.24053, -78.61998, 0.0], [-91.14817, -78.62036, 0.0], [-91.150024, -78.638589, 0.0], [-90.872462, -78.639554, 0.0], [-90.873874, -78.657786, 0.0], [-90.781194, -78.658049, 0.0], [-90.78246, -78.676281, 0.0], [-90.689626, -78.676516, 0.0], [-90.691868, -78.712982, 0.0], [-90.598728, -78.713188, 0.0], [-90.599703, -78.731422, 0.0], [-90.506409, -78.731598, 0.0], [-90.508064, -78.76807, 0.0], [-90.414462, -78.768217, 0.0], [-90.41582, -78.804691, 0.0], [-90.32191, -78.804808, 0.0], [-90.324034, -78.877764, 0.0], [-90.229502, -78.877852, 0.0], [-90.230262, -78.914333, 0.0], [-90.040568, -78.914419, 0.0], [-90.040635, -78.932661, 0.0], [-89.94563, -78.932659, 0.0], [-89.94554, -78.950901, 0.0], [-89.850378, -78.950868, 0.0], [-89.850129, -78.969111, 0.0], [-89.754809, -78.969048, 0.0], [-89.75399, -79.005535, 0.0], [-89.562719, -79.005317, 0.0], [-89.561988, -79.023561, 0.0], [-89.466196, -79.023406, 0.0], [-89.465302, -79.04165, 0.0], [-89.273406, -79.041249, 0.0], [-89.272187, -79.059493, 0.0], [-88.983893, -79.05866, 0.0], [-88.982186, -79.076903, 0.0], [-89.1747, -79.07749, 0.0], [-89.173311, -79.095734, 0.0], [-89.269737, -79.095982, 0.0], [-89.268506, -79.114228, 0.0], [-89.365099, -79.114445, 0.0], [-89.364027, -79.132691, 0.0], [-89.460787, -79.132879, 0.0], [-89.458959, -79.169374, 0.0], [-89.55605, -79.16953, 0.0], [-89.555296, -79.187779, 0.0], [-89.652554, -79.187905, 0.0], [-89.651963, -79.206154, 0.0], [-89.749389, -79.20625, 0.0], [-89.748962, -79.2245, 0.0], [-89.846555, -79.224564, 0.0], [-89.846293, -79.242815, 0.0], [-90.041814, -79.24285, 0.0], [-90.042029, -79.297606, 0.0], [-90.140292, -79.297577, 0.0], [-90.140775, -79.334083, 0.0], [-90.042173, -79.334112, 0.0], [-90.042319, -79.37062, 0.0], [-90.141261, -79.370591, 0.0], [-90.141505, -79.388846, 0.0], [-90.240618, -79.388785, 0.0], [-90.241873, -79.443552, 0.0], [-90.341501, -79.443459, 0.0], [-90.342693, -79.479973, 0.0], [-90.442666, -79.479848, 0.0], [-90.444995, -79.534621, 0.0], [-90.545492, -79.534464, 0.0], [-90.546451, -79.552722, 0.0], [-90.445777, -79.55288, 0.0], [-90.447349, -79.5894, 0.0], [-91.053456, -79.587965, 0.0], [-91.055316, -79.606223, 0.0], [-91.257663, -79.605486, 0.0], [-91.259887, -79.623743, 0.0], [-91.361228, -79.623325, 0.0], [-91.36364, -79.641582, 0.0], [-91.465152, -79.641131, 0.0], [-91.488897, -79.805457, 0.0], [-91.695178, -79.804442, 0.0], [-91.698235, -79.822701, 0.0], [-91.801545, -79.822143, 0.0], [-91.808067, -79.85866, 0.0], [-91.704384, -79.85922, 0.0], [-91.707475, -79.87748, 0.0], [-91.811346, -79.876919, 0.0], [-91.814637, -79.895179, 0.0], [-91.918685, -79.894584, 0.0], [-91.922176, -79.912843, 0.0], [-92.026401, -79.912214, 0.0], [-92.030095, -79.930472, 0.0], [-92.134495, -79.929808, 0.0], [-92.138393, -79.948066, 0.0], [-92.347532, -79.946636, 0.0], [-92.351826, -79.964891, 0.0], [-92.456562, -79.964125, 0.0], [-92.461064, -79.982379, 0.0], [-92.565975, -79.981578, 0.0], [-92.570685, -79.999832, 0.0], [-92.78084, -79.998126, 0.0], [-92.785952, -80.016376, 0.0], [-92.891195, -80.015471, 0.0], [-92.896519, -80.033721, 0.0], [-93.001935, -80.032781, 0.0], [-93.007473, -80.051029, 0.0], [-93.113062, -80.050053, 0.0], [-93.118814, -80.0683, 0.0], [-93.224577, -80.067288, 0.0], [-93.230546, -80.085534, 0.0], [-93.336481, -80.084487, 0.0], [-93.324176, -80.048001, 0.0], [-93.429699, -80.046925, 0.0], [-93.417099, -80.010444, 0.0], [-93.522213, -80.009338, 0.0], [-93.515756, -79.991101, 0.0], [-93.620655, -79.989964, 0.0], [-93.61403, -79.971729, 0.0], [-93.718714, -79.97056, 0.0], [-93.711924, -79.952328, 0.0], [-93.816393, -79.951128, 0.0], [-93.788723, -79.87821, 0.0], [-93.892414, -79.876987, 0.0], [-93.864399, -79.804083, 0.0], [-93.967323, -79.802836, 0.0], [-93.946026, -79.748169, 0.0], [-93.843651, -79.749409, 0.0], [-93.823125, -79.694739, 0.0], [-93.924956, -79.693505, 0.0], [-93.90411, -79.638844, 0.0], [-94.005379, -79.637584, 0.0], [-93.998302, -79.619367, 0.0], [-94.099369, -79.618077, 0.0], [-94.092139, -79.599863, 0.0], [-94.193003, -79.598544, 0.0], [-94.185623, -79.580332, 0.0], [-94.386921, -79.577602, 0.0], [-94.379215, -79.559395, 0.0], [-94.680431, -79.555069, 0.0], [-94.672229, -79.53687, 0.0], [-94.772403, -79.535367, 0.0], [-94.747448, -79.48078, 0.0], [-94.847075, -79.479253, 0.0], [-94.81352, -79.406486, 0.0], [-94.912434, -79.404938, 0.0], [-94.903948, -79.38675, 0.0], [-95.101351, -79.383566, 0.0], [-95.092557, -79.365384, 0.0], [-95.191045, -79.363748, 0.0], [-95.155505, -79.291032, 0.0], [-95.253295, -79.289376, 0.0], [-95.244321, -79.271201, 0.0], [-95.341915, -79.269517, 0.0], [-95.332806, -79.251344, 0.0], [-95.430206, -79.249633, 0.0], [-95.420964, -79.231464, 0.0], [-95.323729, -79.233172, 0.0], [-95.269903, -79.124145, 0.0], [-95.366167, -79.122454, 0.0], [-95.357141, -79.104287, 0.0], [-95.453215, -79.102568, 0.0], [-95.425842, -79.048076, 0.0], [-95.616944, -79.044565, 0.0], [-95.598218, -79.00825, 0.0], [-95.693408, -79.006456, 0.0], [-95.683935, -78.988302, 0.0], [-95.588901, -78.990093, 0.0], [-95.579615, -78.971937, 0.0], [-95.484707, -78.973695, 0.0], [-95.475607, -78.955536, 0.0], [-95.380824, -78.957262, 0.0], [-95.37191, -78.9391, 0.0], [-95.466538, -78.937377, 0.0], [-95.457498, -78.919218, 0.0], [-95.551942, -78.917468, 0.0], [-95.542778, -78.899312, 0.0], [-95.637038, -78.897535, 0.0], [-95.609268, -78.843079, 0.0], [-95.515467, -78.844846, 0.0], [-95.506423, -78.826692, 0.0], [-95.412744, -78.828427, 0.0], [-95.403881, -78.81027, 0.0], [-95.310325, -78.811973, 0.0], [-95.301642, -78.793813, 0.0], [-95.114747, -78.797124, 0.0], [-95.106394, -78.778959, 0.0], [-95.013057, -78.780567, 0.0], [-95.004882, -78.7624, 0.0], [-94.911669, -78.763976, 0.0], [-94.895698, -78.727637, 0.0], [-94.988611, -78.726066, 0.0], [-94.940425, -78.617072, 0.0], [-95.032424, -78.615487, 0.0], [-95.024337, -78.597325, 0.0], [-95.207964, -78.594073, 0.0], [-95.191285, -78.557761, 0.0], [-95.465652, -78.552682, 0.0], [-95.474413, -78.57083, 0.0], [-95.748962, -78.565482, 0.0], [-95.721466, -78.511065, 0.0], [-95.812493, -78.509234, 0.0], [-95.803243, -78.491098, 0.0], [-96.075717, -78.48544, 0.0], [-96.06607, -78.467314, 0.0], [-96.156692, -78.465373, 0.0], [-96.146934, -78.447251, 0.0], [-96.327803, -78.44329, 0.0], [-96.297869, -78.388943, 0.0], [-96.387836, -78.386929, 0.0], [-96.377781, -78.368817, 0.0], [-96.467577, -78.366779, 0.0], [-96.457416, -78.34867, 0.0], [-96.547041, -78.346606, 0.0], [-96.536773, -78.328501, 0.0], [-96.80504, -78.32215, 0.0], [-96.794392, -78.304055, 0.0], [-96.883611, -78.301886, 0.0], [-96.872859, -78.283794, 0.0], [-96.961909, -78.2816, 0.0], [-96.940233, -78.245425, 0.0], [-97.028977, -78.243209, 0.0], [-97.018054, -78.225125, 0.0], [-97.19517, -78.220617, 0.0], [-97.184011, -78.20254, 0.0], [-97.272383, -78.200248, 0.0], [-97.238713, -78.14603, 0.0], [-97.326651, -78.14372, 0.0], [-97.315364, -78.125651, 0.0], [-97.403134, -78.123318, 0.0], [-97.391749, -78.105253, 0.0], [-97.566921, -78.10051, 0.0], [-97.555308, -78.082453, 0.0], [-97.64271, -78.080044, 0.0], [-97.607693, -78.025883, 0.0], [-97.520682, -78.02828, 0.0], [-97.497773, -77.992166, 0.0], [-97.410987, -77.994529, 0.0], [-97.399713, -77.976468, 0.0], [-97.313022, -77.9788, 0.0], [-97.27979, -77.924608, 0.0], [-97.193451, -77.926901, 0.0], [-97.139363, -77.836566, 0.0], [-96.967859, -77.841038, 0.0], [-96.946954, -77.804891, 0.0], [-96.861407, -77.80708, 0.0], [-96.851127, -77.789004, 0.0], [-96.765675, -77.791162, 0.0], [-96.725358, -77.718845, 0.0], [-96.640377, -77.720964, 0.0], [-96.620645, -77.6848, 0.0], [-96.535882, -77.686886, 0.0], [-96.526184, -77.668801, 0.0], [-96.441516, -77.670857, 0.0], [-96.384656, -77.562336, 0.0], [-96.552494, -77.558236, 0.0], [-96.514174, -77.485919, 0.0], [-96.59757, -77.483841, 0.0], [-96.58794, -77.465766, 0.0], [-96.671187, -77.463665, 0.0], [-96.680937, -77.481738, 0.0], [-97.263693, -77.466276, 0.0], [-97.253111, -77.448226, 0.0], [-97.336123, -77.445916, 0.0], [-97.325453, -77.42787, 0.0], [-97.491148, -77.423178, 0.0], [-97.480274, -77.405139, 0.0], [-97.397559, -77.407495, 0.0], [-97.376139, -77.371411, 0.0], [-97.293628, -77.373733, 0.0], [-97.28308, -77.355688, 0.0], [-98.433698, -77.320866, 0.0], [-98.421564, -77.302872, 0.0], [-98.666926, -77.294764, 0.0], [-98.642079, -77.2588, 0.0], [-99.049167, -77.244815, 0.0], [-99.036233, -77.226854, 0.0], [-99.522851, -77.209257, 0.0], [-99.509284, -77.191321, 0.0], [-99.832489, -77.179101, 0.0], [-99.818518, -77.161182, 0.0], [-99.979666, -77.154929, 0.0], [-99.965515, -77.137019, 0.0], [-100.447336, -77.117686, 0.0], [-100.432572, -77.099804, 0.0], [-100.512625, -77.096499, 0.0], [-100.483005, -77.060743, 0.0], [-100.642555, -77.054077, 0.0], [-100.627593, -77.036208, 0.0], [-100.707198, -77.032842, 0.0], [-100.692171, -77.014978, 0.0], [-100.851044, -77.008182, 0.0], [-100.835847, -76.990327, 0.0], [-100.915114, -76.986897, 0.0], [-100.899853, -76.969047, 0.0], [-101.058051, -76.962123, 0.0], [-101.042622, -76.944282, 0.0], [-101.121553, -76.940788, 0.0], [-101.090613, -76.905114, 0.0], [-101.169293, -76.901606, 0.0], [-101.153783, -76.883774, 0.0], [-101.232316, -76.880245, 0.0], [-101.216746, -76.862418, 0.0], [-101.295133, -76.85887, 0.0], [-101.217404, -76.769752, 0.0], [-101.295238, -76.766205, 0.0], [-101.279717, -76.748385, 0.0], [-101.357407, -76.744819, 0.0], [-101.310795, -76.691373, 0.0], [-101.388141, -76.687797, 0.0], [-101.372587, -76.669986, 0.0], [-101.449791, -76.666392, 0.0], [-101.326063, -76.523929, 0.0], [-101.402436, -76.52035, 0.0], [-101.341168, -76.449131, 0.0], [-101.265184, -76.45269, 0.0], [-101.175067, -76.345822, 0.0], [-101.250474, -76.342292, 0.0], [-101.190803, -76.27106, 0.0], [-101.265793, -76.267525, 0.0], [-101.250878, -76.249721, 0.0], [-101.325735, -76.246168, 0.0], [-101.280944, -76.192769, 0.0], [-101.429978, -76.185621, 0.0], [-101.399941, -76.150039, 0.0], [-101.474214, -76.14644, 0.0], [-101.459161, -76.128654, 0.0], [-101.533304, -76.125037, 0.0], [-101.518198, -76.107255, 0.0], [-101.59221, -76.10362, 0.0], [-101.577051, -76.085842, 0.0], [-101.650932, -76.082189, 0.0], [-101.635722, -76.064416, 0.0], [-101.709473, -76.060745, 0.0], [-101.694211, -76.042976, 0.0], [-101.767832, -76.039287, 0.0], [-101.752518, -76.021523, 0.0], [-101.899461, -76.014086, 0.0], [-101.837882, -75.943066, 0.0], [-101.910936, -75.939333, 0.0], [-101.89555, -75.921582, 0.0], [-101.968477, -75.917832, 0.0], [-101.953041, -75.900085, 0.0], [-102.02584, -75.896317, 0.0], [-102.010356, -75.878575, 0.0], [-102.083027, -75.87479, 0.0], [-102.067494, -75.857052, 0.0], [-102.140038, -75.853249, 0.0], [-102.124457, -75.835516, 0.0], [-102.196874, -75.831696, 0.0], [-102.181245, -75.813967, 0.0], [-102.253535, -75.810129, 0.0], [-102.237859, -75.792406, 0.0], [-102.310023, -75.78855, 0.0], [-102.294299, -75.770832, 0.0], [-102.366338, -75.766959, 0.0], [-102.350567, -75.749245, 0.0], [-102.494353, -75.741443, 0.0], [-102.478451, -75.723738, 0.0], [-102.693572, -75.711884, 0.0], [-102.70973, -75.729573, 0.0], [-102.853113, -75.72155, 0.0], [-102.869482, -75.739229, 0.0], [-102.941198, -75.735179, 0.0], [-102.957693, -75.752851, 0.0], [-103.029452, -75.748774, 0.0], [-103.012872, -75.731107, 0.0], [-103.227644, -75.718758, 0.0], [-103.210852, -75.701106, 0.0], [-103.282275, -75.696951, 0.0], [-103.265441, -75.679303, 0.0], [-103.336738, -75.675132, 0.0], [-103.303027, -75.639846, 0.0], [-103.445162, -75.631459, 0.0], [-103.428203, -75.613826, 0.0], [-103.923762, -75.583823, 0.0], [-103.90627, -75.566227, 0.0], [-103.976811, -75.56186, 0.0], [-103.941793, -75.526678, 0.0], [-104.012128, -75.5223, 0.0], [-103.942283, -75.45195, 0.0], [-103.914847, -75.426057, 0.0], [-103.846549, -75.420428, 0.0], [-103.814359, -75.41156, 0.0], [-103.74731, -75.394972, 0.0], [-103.643531, -75.376578, 0.0], [-103.639472, -75.360155, 0.0], [-103.549124, -75.339049, 0.0], [-103.509054, -75.329656, 0.0], [-103.456714, -75.307204, 0.0], [-103.37484, -75.273725, 0.0], [-103.284801, -75.264374, 0.0], [-103.224839, -75.25812, 0.0], [-103.182394, -75.249825, 0.0], [-103.086408, -75.237813, 0.0], [-103.042136, -75.231576, 0.0], [-102.981295, -75.215486, 0.0], [-102.956754, -75.210167, 0.0], [-102.921448, -75.203018, 0.0], [-102.898283, -75.198106, 0.0], [-102.873449, -75.192921, 0.0], [-102.84957, -75.188785, 0.0], [-102.825705, -75.184646, 0.0], [-102.789524, -75.181222, 0.0], [-102.744295, -75.17242, 0.0], [-102.656346, -75.16239, 0.0], [-102.607491, -75.160775, 0.0], [-102.560626, -75.159773, 0.0], [-102.511333, -75.159268, 0.0], [-102.378744, -75.152045, 0.0], [-102.34262, -75.146716, 0.0], [-102.266406, -75.132957, 0.0], [-102.223828, -75.128342, 0.0], [-102.157455, -75.12945, 0.0], [-102.113853, -75.130386, 0.0], [-102.068876, -75.13139, 0.0], [-102.040635, -75.126691, 0.0], [-102.013199, -75.12121, 0.0], [-101.969076, -75.11627, 0.0], [-101.953576, -75.113073, 0.0], [-101.923326, -75.111044, 0.0], [-101.896684, -75.109917, 0.0], [-101.821333, -75.103337, 0.0], [-101.766389, -75.098945, 0.0], [-101.726414, -75.090073, 0.0], [-101.723655, -75.079577, 0.0], [-101.631989, -75.054005, 0.0], [-101.564382, -75.02971, 0.0], [-101.547244, -75.015213, 0.0], [-101.531499, -75.000643, 0.0], [-101.549303, -74.990901, 0.0], [-101.489949, -74.940509, 0.0], [-101.469959, -74.921526, 0.0], [-101.455398, -74.908855, 0.0], [-101.420557, -74.891146, 0.0], [-101.399072, -74.882138, 0.0], [-101.391177, -74.870096, 0.0], [-101.371447, -74.860874, 0.0], [-101.363063, -74.853621, 0.0], [-101.338827, -74.838164, 0.0], [-101.312982, -74.826333, 0.0], [-101.29282, -74.816401, 0.0], [-101.276851, -74.808624, 0.0], [-101.27464, -74.804247, 0.0], [-101.259243, -74.798558, 0.0], [-101.251822, -74.792086, 0.0], [-101.267741, -74.78708, 0.0], [-101.256493, -74.781809, 0.0], [-101.257733, -74.779767, 0.0], [-101.250447, -74.777156, 0.0], [-101.240613, -74.770054, 0.0], [-101.222641, -74.763963, 0.0], [-101.216307, -74.748673, 0.0], [-101.212936, -74.740259, 0.0], [-101.200426, -74.734469, 0.0], [-101.197349, -74.72643, 0.0], [-101.188725, -74.7179, 0.0], [-101.207959, -74.716895, 0.0], [-101.219968, -74.709239, 0.0], [-101.232933, -74.706803, 0.0], [-101.230248, -74.703234, 0.0], [-101.238372, -74.70027, 0.0], [-101.254074, -74.700252, 0.0], [-101.275428, -74.693637, 0.0], [-101.306089, -74.693851, 0.0], [-101.351676, -74.691805, 0.0], [-101.364701, -74.681592, 0.0], [-101.396392, -74.67954, 0.0], [-101.416381, -74.679976, 0.0], [-101.462601, -74.674445, 0.0], [-101.482989, -74.660146, 0.0], [-101.530932, -74.656493, 0.0], [-101.545802, -74.657827, 0.0], [-101.570915, -74.655354, 0.0], [-101.627933, -74.648117, 0.0], [-101.647793, -74.639151, 0.0], [-101.676385, -74.635907, 0.0], [-101.678978, -74.633321, 0.0], [-101.695894, -74.628422, 0.0], [-101.728673, -74.621731, 0.0], [-101.781287, -74.617603, 0.0], [-101.794801, -74.615021, 0.0], [-101.870395, -74.608983, 0.0], [-101.933735, -74.601768, 0.0], [-101.986726, -74.595483, 0.0], [-102.032573, -74.595827, 0.0], [-102.026749, -74.590285, 0.0], [-102.010395, -74.580201, 0.0], [-102.035597, -74.564212, 0.0], [-102.090552, -74.553133, 0.0], [-102.264411, -74.519626, 0.0], [-102.339743, -74.51083, 0.0], [-102.411915, -74.510518, 0.0], [-102.424826, -74.497263, 0.0], [-102.377212, -74.483896, 0.0], [-102.280808, -74.473374, 0.0], [-102.236421, -74.463717, 0.0], [-102.185211, -74.450043, 0.0], [-102.150282, -74.438359, 0.0], [-102.110682, -74.429878, 0.0], [-102.080455, -74.419386, 0.0], [-102.029215, -74.421347, 0.0], [-101.986657, -74.414487, 0.0], [-101.942992, -74.405238, 0.0], [-101.914922, -74.383364, 0.0], [-101.795349, -74.369597, 0.0], [-101.698034, -74.375051, 0.0], [-101.572267, -74.390817, 0.0], [-101.433665, -74.404266, 0.0], [-101.358339, -74.410301, 0.0], [-101.276679, -74.412744, 0.0], [-101.200663, -74.403148, 0.0], [-101.126055, -74.400282, 0.0], [-101.050277, -74.385754, 0.0], [-100.925725, -74.378623, 0.0], [-100.827076, -74.373988, 0.0], [-100.786332, -74.316362, 0.0], [-100.72066, -74.319735, 0.0], [-100.708238, -74.301973, 0.0], [-100.642611, -74.305321, 0.0], [-100.617997, -74.26979, 0.0], [-100.552486, -74.273111, 0.0], [-100.528129, -74.237572, 0.0], [-100.462734, -74.240864, 0.0], [-100.355131, -74.080906, 0.0], [-100.290352, -74.084143, 0.0], [-100.278602, -74.066367, 0.0], [-100.213868, -74.06958, 0.0], [-100.190588, -74.03402, 0.0], [-100.125968, -74.037206, 0.0], [-100.114438, -74.019422, 0.0], [-100.049863, -74.022585, 0.0], [-100.061323, -74.040372, 0.0], [-99.996651, -74.043518, 0.0], [-100.008066, -74.061309, 0.0], [-99.943298, -74.064439, 0.0], [-99.954667, -74.082234, 0.0], [-99.889802, -74.085347, 0.0], [-99.878504, -74.067549, 0.0], [-99.68397, -74.076757, 0.0], [-99.672911, -74.058947, 0.0], [-99.218628, -74.079702, 0.0], [-99.208094, -74.061869, 0.0], [-98.688058, -74.08435, 0.0], [-98.678122, -74.06649, 0.0], [-98.026778, -74.092735, 0.0], [-98.035988, -74.110626, 0.0], [-97.774563, -74.120566, 0.0], [-97.783502, -74.138469, 0.0], [-97.521457, -74.148094, 0.0], [-97.512812, -74.13018, 0.0], [-97.447324, -74.132532, 0.0], [-97.438772, -74.114615, 0.0], [-97.242413, -74.121541, 0.0], [-97.234101, -74.103616, 0.0], [-97.103247, -74.108126, 0.0], [-97.095101, -74.090197, 0.0], [-97.02972, -74.092418, 0.0], [-97.021665, -74.074486, 0.0], [-96.825632, -74.08102, 0.0], [-96.833465, -74.098959, 0.0], [-96.768011, -74.101099, 0.0], [-96.775789, -74.119041, 0.0], [-96.513501, -74.127404, 0.0], [-96.506019, -74.109452, 0.0], [-96.374919, -74.113506, 0.0], [-96.367602, -74.095549, 0.0], [-96.302101, -74.097543, 0.0], [-96.294875, -74.079584, 0.0], [-96.229432, -74.081555, 0.0], [-96.222295, -74.063595, 0.0], [-96.156909, -74.065543, 0.0], [-96.149863, -74.047581, 0.0], [-95.95383, -74.053295, 0.0], [-95.947021, -74.035326, 0.0], [-95.816402, -74.039029, 0.0], [-95.809755, -74.021057, 0.0], [-95.679223, -74.024673, 0.0], [-95.672738, -74.006697, 0.0], [-95.542294, -74.010228, 0.0], [-95.535971, -73.992248, 0.0], [-95.405616, -73.995692, 0.0], [-95.399454, -73.97771, 0.0], [-95.26919, -73.981068, 0.0], [-95.263189, -73.963082, 0.0], [-95.133017, -73.966355, 0.0], [-95.121348, -73.930376, 0.0], [-95.056388, -73.931978, 0.0], [-95.050646, -73.913988, 0.0], [-94.985747, -73.915568, 0.0], [-94.980091, -73.897576, 0.0], [-94.915251, -73.899134, 0.0], [-94.909681, -73.881141, 0.0], [-94.844902, -73.882677, 0.0], [-94.839417, -73.864683, 0.0], [-94.774698, -73.866196, 0.0], [-94.769297, -73.848201, 0.0], [-94.704639, -73.849692, 0.0], [-94.699323, -73.831696, 0.0], [-94.634725, -73.833165, 0.0], [-94.629493, -73.815168, 0.0], [-94.564955, -73.816615, 0.0], [-94.559808, -73.798617, 0.0], [-94.430842, -73.801447, 0.0], [-94.420869, -73.765446, 0.0], [-94.356514, -73.766828, 0.0], [-94.351616, -73.748827, 0.0], [-94.287321, -73.750186, 0.0], [-94.277701, -73.714183, 0.0], [-94.213539, -73.715519, 0.0], [-94.223015, -73.751526, 0.0], [-94.158698, -73.752845, 0.0], [-94.168073, -73.788858, 0.0], [-94.103602, -73.79016, 0.0], [-94.117527, -73.844188, 0.0], [-94.052828, -73.845474, 0.0], [-94.057417, -73.863487, 0.0], [-93.992635, -73.864754, 0.0], [-93.997163, -73.882768, 0.0], [-93.5429, -73.89108, 0.0], [-93.546925, -73.909105, 0.0], [-93.416904, -73.911299, 0.0], [-93.420791, -73.929327, 0.0], [-93.095219, -73.934459, 0.0], [-93.098746, -73.952494, 0.0], [-93.033533, -73.95346, 0.0], [-93.030081, -73.935424, 0.0], [-92.117389, -73.946779, 0.0], [-92.114979, -73.92873, 0.0], [-92.049815, -73.929387, 0.0], [-92.05215, -73.947436, 0.0], [-91.921656, -73.948689, 0.0], [-91.923848, -73.96674, 0.0], [-91.793186, -73.967912, 0.0], [-91.795233, -73.985966, 0.0], [-91.729821, -73.986521, 0.0], [-91.731798, -74.004576, 0.0], [-91.666307, -74.005112, 0.0], [-91.668214, -74.023169, 0.0], [-91.077936, -74.027065, 0.0], [-91.076703, -74.009003, 0.0], [-91.011175, -74.009332, 0.0], [-91.01002, -73.991272, 0.0], [-90.879106, -73.991867, 0.0], [-90.878103, -73.973806, 0.0], [-90.812717, -73.974073, 0.0], [-90.811791, -73.956012, 0.0], [-90.746478, -73.956258, 0.0], [-90.74733, -73.974319, 0.0], [-90.551155, -73.974933, 0.0], [-90.551785, -73.992995, 0.0], [-90.486316, -73.993159, 0.0], [-90.486872, -74.011222, 0.0], [-90.290232, -74.011589, 0.0], [-90.290565, -74.029653, 0.0], [-90.159318, -74.029795, 0.0], [-90.1595, -74.047861, 0.0], [-90.028101, -74.04792, 0.0], [-90.028133, -74.065986, 0.0], [-89.830808, -74.065919, 0.0], [-89.830418, -74.102053, 0.0], [-89.764492, -74.10199, 0.0], [-89.764221, -74.120058, 0.0], [-89.69822, -74.119973, 0.0], [-89.697523, -74.156112, 0.0], [-89.63137, -74.156006, 0.0], [-89.630517, -74.192147, 0.0], [-89.564212, -74.19202, 0.0], [-89.563707, -74.210092, 0.0], [-89.430947, -74.209775, 0.0], [-89.430287, -74.227847, 0.0], [-89.29738, -74.227445, 0.0], [-89.296564, -74.245518, 0.0], [-89.230036, -74.245285, 0.0], [-89.22914, -74.263358, 0.0], [-89.162537, -74.263104, 0.0], [-89.161562, -74.281178, 0.0], [-89.028207, -74.280607, 0.0], [-89.02594, -74.316754, 0.0], [-88.892285, -74.316097, 0.0], [-88.890991, -74.334171, 0.0], [-88.82409, -74.333811, 0.0], [-88.822715, -74.351885, 0.0], [-88.688766, -74.3511, 0.0], [-88.687231, -74.369174, 0.0], [-88.620184, -74.368749, 0.0], [-88.618567, -74.386824, 0.0], [-88.484327, -74.38591, 0.0], [-88.482549, -74.403984, 0.0], [-88.348167, -74.402984, 0.0], [-88.346228, -74.421057, 0.0], [-88.278965, -74.420525, 0.0], [-88.276942, -74.438598, 0.0], [-88.142273, -74.437468, 0.0], [-88.140087, -74.455541, 0.0], [-88.072681, -74.454944, 0.0], [-88.07041, -74.473017, 0.0], [-87.935456, -74.471756, 0.0], [-87.93302, -74.489828, 0.0], [-87.865472, -74.489165, 0.0], [-87.862952, -74.507237, 0.0], [-87.79533, -74.506552, 0.0], [-87.792724, -74.524624, 0.0], [-87.65734, -74.523188, 0.0], [-87.654567, -74.541259, 0.0], [-87.586805, -74.540508, 0.0], [-87.583946, -74.558579, 0.0], [-87.51611, -74.557806, 0.0], [-87.513164, -74.575876, 0.0], [-87.241573, -74.572566, 0.0], [-87.238298, -74.590633, 0.0], [-87.034444, -74.587922, 0.0], [-87.03092, -74.605986, 0.0], [-86.962905, -74.605038, 0.0], [-86.955671, -74.641167, 0.0], [-86.887503, -74.640195, 0.0], [-86.868859, -74.730522, 0.0], [-86.800293, -74.729523, 0.0], [-86.792609, -74.765656, 0.0], [-86.723889, -74.764633, 0.0], [-86.716003, -74.800766, 0.0], [-86.647127, -74.799719, 0.0], [-86.63091, -74.871988, 0.0], [-86.561712, -74.870913, 0.0], [-86.553377, -74.907049, 0.0], [-86.622742, -74.908126, 0.0]])
    obs = apifmt._fmt_spatial('polygon', poly)
    exp = {'polygon': '-86.622742,-74.908126,-86.561712,-74.870913,-86.868859,-74.730522,-86.962905,-74.605038,-89.02594,-74.316754,-89.630517,-74.192147,-89.830808,-74.065919,-90.746478,-73.956258,-91.668214,-74.023169,-92.049815,-73.929387,-93.420791,-73.929327,-93.997163,-73.882768,-94.277701,-73.714183,-95.133017,-73.966355,-96.513501,-74.127404,-99.889802,-74.085347,-100.114438,-74.019422,-100.355131,-74.080906,-100.462734,-74.240864,-100.827076,-74.373988,-101.795349,-74.369597,-102.424826,-74.497263,-101.188725,-74.7179,-101.564382,-75.02971,-103.37484,-75.273725,-103.914847,-75.426057,-104.012128,-75.5223,-103.029452,-75.748774,-102.350567,-75.749245,-101.837882,-75.943066,-101.899461,-76.014086,-101.280944,-76.192769,-101.325735,-76.246168,-101.190803,-76.27106,-101.250474,-76.342292,-101.175067,-76.345822,-101.402436,-76.52035,-101.326063,-76.523929,-101.449791,-76.666392,-101.310795,-76.691373,-101.357407,-76.744819,-101.217404,-76.769752,-101.295133,-76.85887,-101.058051,-76.962123,-100.447336,-77.117686,-98.433698,-77.320866,-97.28308,-77.355688,-97.491148,-77.423178,-96.514174,-77.485919,-96.552494,-77.558236,-96.384656,-77.562336,-96.441516,-77.670857,-97.139363,-77.836566,-97.193451,-77.926901,-97.64271,-78.080044,-96.297869,-78.388943,-96.327803,-78.44329,-95.721466,-78.511065,-95.748962,-78.565482,-94.940425,-78.617072,-94.988611,-78.726066,-94.911669,-78.763976,-95.609268,-78.843079,-95.637038,-78.897535,-95.37191,-78.9391,-95.693408,-79.006456,-95.269903,-79.124145,-95.323729,-79.233172,-95.430206,-79.249633,-95.155505,-79.291032,-95.191045,-79.363748,-94.81352,-79.406486,-94.847075,-79.479253,-94.747448,-79.48078,-94.772403,-79.535367,-93.90411,-79.638844,-93.843651,-79.749409,-93.967323,-79.802836,-93.788723,-79.87821,-93.816393,-79.951128,-93.230546,-80.085534,-91.707475,-79.87748,-91.801545,-79.822143,-91.488897,-79.805457,-91.465152,-79.641131,-90.447349,-79.5894,-90.545492,-79.534464,-90.042319,-79.37062,-90.140775,-79.334083,-90.041814,-79.24285,-88.982186,-79.076903,-90.230262,-78.914333,-90.32191,-78.804808,-90.689626,-78.676516,-91.150024,-78.638589,-92.035347,-78.414844,-92.106013,-78.30491,-91.651645,-78.271472,-91.365784,-78.127206,-91.188783,-78.128018,-91.090167,-78.019109,-90.737076,-77.983849,-90.909191,-77.946905,-90.732603,-77.911009,-90.727088,-77.819973,-91.070502,-77.800626,-91.14118,-77.636469,-91.90279,-77.613923,-91.984627,-77.595116,-91.972963,-77.522365,-92.466819,-77.463587,-92.199521,-77.374914,-92.352136,-77.300761,-92.335283,-77.209895,-91.434206,-77.234653,-91.426015,-77.16193,-91.015545,-77.145686,-91.008355,-77.054784,-91.086397,-77.018096,-91.647835,-76.97871,-91.640906,-76.924199,-91.873848,-76.868024,-91.779021,-76.759619,-90.823937,-76.710073,-90.345113,-76.52953,-86.988029,-75.856983,-86.945563,-75.711143,-86.872234,-75.710165,-87.034102,-75.63967,-86.965004,-75.620616,-87.075115,-75.440545,-87.003154,-75.439609,-87.021872,-75.349129,-86.835058,-75.219586,-86.850654,-75.147247,-86.717729,-75.109052,-86.737771,-75.018662,-86.602149,-74.998483,-86.622742,-74.908126'}
    assert obs == exp


########## _fmt_var_subset_list ##########
def test_var_subset_list_fmt():
    obs = apifmt._fmt_var_subset_list({'atlas_sdp_gps_epoch': ['ancillary_data/atlas_sdp_gps_epoch'],
        'data_end_utc': ['ancillary_data/data_end_utc'],
        'data_start_utc': ['ancillary_data/data_start_utc'],
        'end_delta_time': ['ancillary_data/end_delta_time'],
        'granule_end_utc': ['ancillary_data/granule_end_utc'],
        'granule_start_utc': ['ancillary_data/granule_start_utc'],
        'latitude': ['profile_2/high_rate/latitude', 'profile_2/low_rate/latitude'],
        'sc_orient': ['orbit_info/sc_orient'],
        'start_delta_time': ['ancillary_data/start_delta_time']})
    exp = '/ancillary_data/atlas_sdp_gps_epoch,/ancillary_data/data_end_utc,/ancillary_data/data_start_utc,/ancillary_data/end_delta_time,/ancillary_data/granule_end_utc,/ancillary_data/granule_start_utc,/profile_2/high_rate/latitude,/profile_2/low_rate/latitude,/orbit_info/sc_orient,/ancillary_data/start_delta_time'
    assert obs == exp


########## combine_params ##########
def test_combine_params():
    dict1 = {'key1': 0, 'key2': 1}
    dict2 = {'key3':10}
    obs = apifmt.combine_params(dict1,dict2)
    expected = {'key1': 0, 'key2': 1, 'key3':10}
    assert obs == expected


########## Parameters (class) ##########

