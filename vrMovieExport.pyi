from builtins import NoneType
from typing import Any
from vrOSGTypes import Vec2f

__name__: str
__doc__: NoneType
__package__: str
__spec__: ModuleSpec

def __loader__(self) -> None: ...
def createMovie(
    self,
    movie: Any,
    filename: str,
    width: int,
    height: int,
    fps: int,
    startFrame: int,
    stopFrame: int,
    ssf: int,
    alpha: bool,
    alphaRed: float,
    alphaGreen: float,
    alphaBlue: float,
    overwrite: bool,
    alpha_premultiply: bool,
    step: int,
    tonemap_hdr: bool,
) -> None: ...
def createSnapshot(
    self,
    filename: str,
    width: int,
    height: int,
    ssf: int,
    alpha: bool,
    alphaRed: float,
    alphaGreen: float,
    alphaBlue: float,
    dpi: float,
    overwrite: bool,
    showImage: bool,
    alpha_premultiply: bool,
    tonemap_hdr: bool,
) -> None: ...
def createSnapshotFast(self, filename: str) -> None: ...
def createSnapshotFastInit(self, width: int, height: int, ssf: int) -> None: ...
def createSnapshotFastTerminate(self) -> None: ...
def createSnapshotStream(self) -> None: ...
def getDepthMode(self) -> int: ...
def getDepthRange(self) -> Vec2f: ...
def getExportExrHalf(self) -> bool: ...
def getExportMultiLayer(self) -> bool: ...
def getExportTiffHDR(self) -> bool: ...
def getLastRenderTime(self) -> None: ...
def getOcclusionRange(self) -> Vec2f: ...
def imageStream(self) -> None: ...
def imageStreamBase64(self) -> None: ...
def renderAnimation(
    self,
    animation: str,
    filename: str,
    width: int,
    height: int,
    fps: int,
    startFrame: int,
    stopFrame: int,
    ssf: int,
    alpha: bool,
    alphaRed: float,
    alphaGreen: float,
    alphaBlue: float,
    overwrite: bool,
    alpha_premultiply: bool,
    tonemap_hdr: bool,
) -> None: ...
def renderStepAnimation(
    self,
    animation: str,
    filename: str,
    width: int,
    height: int,
    fps: int,
    startFrame: int,
    stopFrame: int,
    ssf: int,
    alpha: bool,
    alphaRed: float,
    alphaGreen: float,
    alphaBlue: float,
    overwrite: bool,
    alpha_premultiply: bool,
    step: int,
) -> None: ...
def resetActiveSnapshotMovieRenderPasses(self) -> None: ...
def setActiveSnapshotMovieRenderPasses(
    self,
    beauty_pass: bool,
    diffuse_ibl_pass: bool,
    diffuse_light_pass: bool,
    glossy_ibl_pass: bool,
    glossy_light_pass: bool,
    specular_reflection_pass: bool,
    specular_light_pass: bool,
    translucency_pass: bool,
    incandescence_pass: bool,
    diffuse_indirect_pass: bool,
    glossy_indirect_pass: bool,
    occlusion_pass: bool,
    normal_pass: bool,
    depth_pass: bool,
    material_id_pass: bool,
) -> None: ...
def setAuxiliaryChannelsRenderPasses(
    self,
    occlusion_pass: bool,
    normal_pass: bool,
    depth_pass: bool,
    material_id_pass: bool,
    mask_pass: bool,
    position_pass: bool,
    view_vector_pass: bool,
    crypto_object_pass: bool,
    crypto_object_pass2: bool,
) -> None: ...
def setCombinedChannelsRenderPasses(
    self,
    beauty_pass: bool,
    diffuse_ibl_pass: bool,
    diffuse_light_pass: bool,
    glossy_ibl_pass: bool,
    glossy_light_pass: bool,
    specular_reflection_pass: bool,
    translucency_pass: bool,
    incandescence_pass: bool,
    diffuse_indirect_pass: bool,
    glossy_indirect_pass: bool,
    transparency_pass: bool,
    background_pass: bool,
    volume_pass: bool,
) -> None: ...
def setDepthMode(self, depthMode: int) -> None: ...
def setDepthRange(self, min: float, max: float) -> None: ...
def setExportExrHalf(self, on: bool) -> None: ...
def setExportMultiLayer(self, on: bool) -> None: ...
def setExportTiffHDR(self, on: bool) -> None: ...
def setIlluminationChannelsRenderPasses(
    self,
    diffuse_ibl_pass: bool,
    glossy_ibl_pass: bool,
    translucency_ibl_pass: bool,
    diffuse_light_pass: bool,
    glossy_light_pass: bool,
    translucency_light_pass: bool,
    diffuse_indirect_pass: bool,
    glossy_indirect_pass: bool,
    specular_indirect_pass: bool,
    translucency_indirect_pass: bool,
) -> None: ...
def setImageProcessingRenderPasses(self, fog_pass: bool, lens_flare_pass: bool, backplate_pass: bool, frontplate_pass: bool) -> None: ...
def setMaterialChannelsRenderPasses(
    self,
    diffuse_material_pass: bool,
    glossy_material_pass: bool,
    specular_material_pass: bool,
    translucency_material_pass: bool,
    translucency_material_pass2: bool,
    transparency_material_pass: bool,
) -> None: ...
def setOcclusionRange(self, min: float, max: float) -> None: ...
def setSnapshotEmbedMetaData(
    self,
    embedRenderSettings: bool,
    embedCameraSettings: bool,
    embedNodeVisibilities: bool,
    embedSwitchNodeStates: bool,
    embedSwitchMaterialStates: bool,
) -> None: ...
def setSnapshotICCProfile(self, profileID: int) -> None: ...
def setSnapshotNoShowImage(self, state: bool) -> None: ...
def setSnapshotQuality(self, quality: int) -> None: ...
