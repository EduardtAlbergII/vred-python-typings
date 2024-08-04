from builtins import NoneType
from vrNodePtr import vrNodePtr, NodePtr
from vrMaterialPtr import MaterialPtr, vrMaterialPtr
from vrOSGTypes import Pnt3f, Color3f, Vec3f
from typing import Any

__name__: str
__doc__: str
__package__: str
__spec__: ModuleSpec
VR_STEREO_SPLIT_TOP_BOTTOM: int
VR_STEREO_SPLIT_LEFT_RIGHT: int
VR_STEREO_LEFT_EYE: int
VR_STEREO_RIGHT_EYE: int
VR_STEREO_DOUBLEBUFFER: int
VR_STEREO_REDCYAN: int
VR_STEREO_BLUEYELLOW: int
VR_STEREO_GREENMAGENTA: int
VR_STEREO_HORIZONTALINTERLACED: int
VR_STEREO_VERTICALINTERLACED: int
VR_STEREO_5VIEWS: int
VR_DISPLAY_STANDARD: int
VR_DISPLAY_OCULUS_RIFT: int
VR_DISPLAY_SONY_10BIT: int
VR_DISPLAY_SIM2_HDR: int
VR_DISPLAY_OPEN_VR: int
VR_DISPLAY_HDR10: int
VR_DISPLAY_VARJO: int
VR_DISPLAY_OPEN_XR: int
VR_SS_QUALITY_OFF: int
VR_SS_QUALITY_ON: int
VR_SS_QUALITY_LOW: int
VR_SS_QUALITY_MEDIUM: int
VR_SS_QUALITY_HIGH: int
VR_SS_QUALITY_ULTRA_HIGH: int
VR_QUALITY_ANALYTIC_LOW: int
VR_QUALITY_ANALYTIC_HIGH: int
VR_QUALITY_REALISTIC_LOW: int
VR_QUALITY_REALISTIC_HIGH: int
VR_QUALITY_RAYTRACING: int
VR_QUALITY_NPR: int
VR_DLSS_OFF: int
VR_DLSS_PERFORMANCE: int
VR_DLSS_BALANCED: int
VR_DLSS_QUALITY: int
VR_DLSS_ULTRA_PERFORMANCE: int
VR_DOWNSCALE_FACTOR_LOW: int
VR_DOWNSCALE_FACTOR_MEDIUM: int
VR_DOWNSCALE_FACTOR_HIGH: int
OcclusionCullingAccurate: int
OcclusionCullingFast: int
OcclusionStopAndWait: int
OcclusionMultiFrame: int
OcclusionHierarchicalMultiFrame: int
BEAUTY_PASS: int
DIFFUSE_IBL_LAYER: int
DIFFUSE_LIGHT_COLOR_LAYER: int
GLOSSY_IBL_LAYER: int
GLOSSY_LIGHT_COLOR_LAYER: int
SPECULAR_IBL_LAYER: int
SPECULAR_REFLECTION_LAYER: int
TRANSLUCENCY_LAYER: int
INCANDESCENCE_LAYER: int
DIFFUSE_INDIRECT_LIGHT_LAYER: int
GLOSSY_INDIRECT_LIGHT_LAYER: int
DIFFUSE_MATERIAL_COLOR_LAYER: int
GLOSSY_MATERIAL_COLOR_LAYER: int
SPECULAR_MATERIAL_COLOR_LAYER: int
TRANSLUCENCY_MATERIAL_COLOR_LAYER: int
TRANSPARENCY_MATERIAL_COLOR_LAYER: int
BACKGROUND_MATERIAL_COLOR_LAYER: int
DIFFUSE_IBL_ILLUMINATION_LAYER: int
GLOSSY_IBL_ILLUMINATION_LAYER: int
TRANSLUCENCY_IBL_ILLUMINATION_LAYER: int
DIFFUSE_LIGHT_ILLUMINATION_LAYER: int
GLOSSY_LIGHT_ILLUMINATION_LAYER: int
TRANSLUCENCY_LIGHT_ILLUMINATION_LAYER: int
DIFFUSE_INDIRECT_ILLUMINATION_LAYER: int
GLOSSY_INDIRECT_ILLUMINATION_LAYER: int
SPECULAR_INDIRECT_ILLUMINATION_LAYER: int
TRANSLUCENCY_INDIRECT_ILLUMINATION_LAYER: int
FOG_LAYER: int
LENS_FLARE_LAYER: int
BACKPLATE_LAYER: int
FRONTPLATE_LAYER: int
ENV_OCCLUSION_LAYER: int
VOLUME_COLOR_LAYER: int
NORMAL_LAYER: int
DEPTH_LAYER: int
MATERIAL_ID_LAYER: int
MASK_LAYER: int
POSITION_LAYER: int
VIEW_VECTOR_LAYER: int
VR_SELECT_OBJECT: int
VR_SELECT_COMPONENT: int
VR_SELECT_GROUP: int
VR_SELECT_BY_MATERIAL: int
VR_SELECT_ADJACENT: int
VR_BAKED_SHADOWS: int
VR_BAKED_BASE_ILLUMINATION: int
VR_BAKED_SEPARATE_ILLUMINATION: int

def __loader__(self) -> None: ...
def adaptZeroParallaxDistance(self, index: int) -> None: ...
def addRenderOverlay(self) -> None: ...
def cancelAntialiasing(self) -> None: ...
def clearRecordedStatistics(self, index: int) -> None: ...
def compressTextures(self) -> None: ...
def createBackplate(self) -> None: ...
def createRenderWindow(self) -> None: ...
def createScreenshot(self, filename: str) -> None: ...
def deleteBackplate(self) -> None: ...
def destroyRenderWindow(self, index: int) -> None: ...
def enableAntialiasing(self, switch: int) -> None: ...
def enableBackplates(self) -> None: ...
def enableDrawAction(self, index: int, state: bool) -> None: ...
def enableFrontplates(self) -> None: ...
def enableHeadlight(self, switch: int) -> None: ...
def enablePowerwall(self, window: int, state: bool) -> bool: ...
def enableRaytracing(self, state: bool) -> None: ...
def enableRaytracingDownscale(self, switch: int) -> None: ...
def enableRender(self, switch: bool) -> None: ...
def enableRenderRegion(self, s: int) -> None: ...
def enableSceneplates(self) -> None: ...
def enableStereo(self, window: int, state: bool, passive: bool, mode: int, es: float, zp: float) -> bool: ...
def getAntialiasingEnabled(self) -> bool: ...
def getAspect(self) -> float: ...
def getAt(self, index: int) -> Pnt3f: ...
def getAuxiliaryNodesVisibleDuringAntialiasing(self) -> bool: ...
def getAverageFPS(self) -> float: ...
def getBackplateMaterial(self) -> None: ...
def getBackplatesEnabled(self) -> None: ...
def getCamNode(self, index: int) -> vrNodePtr: ...
def getCameraPivotAlwaysVisible(self) -> bool: ...
def getCameraPivotVisible(self) -> bool: ...
def getDLSSQuality(self) -> int: ...
def getDepthPeeling(self) -> bool: ...
def getDepthPeelingLayers(self) -> int: ...
def getDollySpeed(self) -> None: ...
def getFPS(self) -> float: ...
def getFar(self) -> float: ...
def getFov(self) -> float: ...
def getFrom(self, index: int) -> Pnt3f: ...
def getFrontplatesEnabled(self) -> None: ...
def getGenlockingFrameCount(self) -> int: ...
def getHeightAboveGround(self) -> None: ...
def getInteractionMode(self) -> None: ...
def getInternalBackplateMaterial(self) -> None: ...
def getLastPickingMaterial(self) -> vrMaterialPtr: ...
def getLastPickingNode(self) -> vrNodePtr: ...
def getLastPickingPosition(self) -> Pnt3f: ...
def getLightmapGPUTextureCompression(self) -> bool: ...
def getMotionFactor(self) -> float: ...
def getMousePosition(self, index: int) -> list: ...
def getNavigationPivot(self, index: int) -> Pnt3f: ...
def getNavigationSpeedMode(self) -> None: ...
def getNear(self) -> float: ...
def getNodeMaterial(self, node: NodePtr) -> MaterialPtr: ...
def getOculusRiftTrackingOrigin(self) -> Pnt3f: ...
def getOculusRiftTrackingOriginType(self) -> int: ...
def getPanningSpeed(self) -> None: ...
def getRaytracingDownscaleFactor(self) -> int: ...
def getRaytracingEnabled(self) -> bool: ...
def getRenderRoot(self, index: int) -> vrNodePtr: ...
def getRenderRoots(self, index: int) -> list: ...
def getRenderWindowCount(self) -> int: ...
def getRenderWindowHeight(self, i: int) -> int: ...
def getRenderWindowWidth(self, i: int) -> int: ...
def getRoll(self, index: int) -> float: ...
def getSAAWindow(self) -> int: ...
def getSceneIntersection(self) -> None: ...
def getSceneplatesEnabled(self) -> None: ...
def getSeparateBakeColor(self) -> Color3f: ...
def getSeparateBakeIntensity(self) -> float: ...
def getShadowMapUpdates(self) -> bool: ...
def getShadowPlane(self, rootNode: NodePtr, shadowPlaneNameRegexp: const) -> None: ...
def getShowASides(self) -> bool: ...
def getShowBSides(self) -> bool: ...
def getSuperSampling(self) -> bool: ...
def getSuperSamplingQuality(self) -> int: ...
def getUp(self, index: int) -> Vec3f: ...
def getUseBake(self, bakeComponent: int) -> bool: ...
def getUseBindless(self) -> bool: ...
def getUseCommandList(self) -> bool: ...
def getUseMulticastSLI(self) -> bool: ...
def getUsePivotBasedPanning(self) -> None: ...
def getUseSinglePassStereo(self) -> bool: ...
def getUseVariableRateShading(self) -> None: ...
def getUserCameraMatrix(self) -> None: ...
def getUserMatrix(self, id: int) -> list: ...
def getUserNode(self) -> None: ...
def getVariableRateShadingMode(self) -> None: ...
def getVariableRateShadingQuality(self) -> None: ...
def getViewAt(self, index: int) -> Pnt3f: ...
def getViewRay(self, index: int, xCoord: int, yCoord: int) -> tuple: ...
def hideBanner(self) -> None: ...
def isRaytracingDownscaleEnabled(self) -> bool: ...
def moveRenderWindow(self, index: int, xPos: int, yPos: int) -> None: ...
def moveStatistic(self, x: int, y: int) -> None: ...
def refreshAllGLObjects(self) -> None: ...
def reinitializeAllGLObjects(self) -> None: ...
def resetGenlockingFrameCount(self) -> None: ...
def resetHMDPose(self) -> None: ...
def resetIsolateView(self, index: int) -> None: ...
def resetNodeMaterial(self, node: NodePtr) -> None: ...
def resetNodeMaterials(self) -> None: ...
def resetOculusRiftOrientation(self) -> None: ...
def resetRenderRoots(self) -> None: ...
def resizeRenderWindow(self, index: int, width: int, height: int) -> None: ...
def setAORendering(self, state: int) -> None: ...
def setAOShadowsVisible(self, state: int) -> None: ...
def setActiveRenderPass(self, passID: Any, index: int) -> None: ...
def setAllGradientBackgrounds(self, colors: list, ints: list) -> None: ...
def setAllNavigationsEnabled(self, state: bool) -> None: ...
def setAnalyticRendering(self, state: int) -> None: ...
def setAspect(self, aspect: float) -> None: ...
def setAt(self, index: int, point: Pnt3f, x: float, y: float, z: float) -> None: ...
def setAutoFrustum(self, switch: int) -> None: ...
def setAuxiliaryNodesVisibleDuringAntialiasing(self, state: bool) -> None: ...
def setBackfaceCulling(self, switch: int) -> None: ...
def setBackplate(self) -> None: ...
def setCameraBeacon(self) -> None: ...
def setCameraConstraint(self, camera_constraint: NodePtr, min_dist: float) -> None: ...
def setCameraHeightAboveGround(self) -> None: ...
def setCameraPanning(self, x: float, y: float) -> None: ...
def setCameraPivotAlwaysVisible(self, state: bool) -> None: ...
def setCameraPivotVisible(self, state: bool) -> None: ...
def setCameraRotation(self, x: float, y: float) -> None: ...
def setCameraScale(self, x: float, y: float, z: float) -> None: ...
def setCameraZUp(self, state: bool) -> None: ...
def setCameraZoom(self, distance: float) -> None: ...
def setClusterCameraConnection(self, state: bool) -> None: ...
def setCorrectDoubleSidedLighting(self) -> None: ...
def setDLSSQuality(self, quality: int) -> None: ...
def setDefaultCameraBeacons(self) -> None: ...
def setDepthOnlyPass(self, switch: int) -> None: ...
def setDepthPeeling(self, state: bool) -> None: ...
def setDepthPeelingLayers(self, layers: int) -> None: ...
def setDiscontinuityRendering(self, state: int) -> None: ...
def setDisplayMode(self, mode: int) -> None: ...
def setDistance(self, index: int, distance: float) -> None: ...
def setDollySpeed(self, scalefactor: float) -> None: ...
def setDoubleSidedLighting(self) -> None: ...
def setEvaluateClipping(self, state: bool) -> None: ...
def setEyeSeparation(self, es: float) -> None: ...
def setFaceNormalRendering(self, state: int) -> None: ...
def setFar(self, far: float) -> None: ...
def setFixedRenderWindowSize(self, width: int, height: int) -> None: ...
def setFlyMode(self, switch: int) -> None: ...
def setForceTransparentObjectSelection(self, mode: Any) -> None: ...
def setFov(self, fov: float) -> None: ...
def setFreezeOcclusionCulling(self, freezeCulling: bool) -> None: ...
def setFrom(self, index: int, point: Pnt3f, x: float, y: float, z: float) -> None: ...
def setFromAtUp(
    self,
    index: int,
    from1: Pnt3f,
    at: Pnt3f,
    up: Vec3f,
    fx: float,
    fy: float,
    fz: float,
    ax: float,
    ay: float,
    az: float,
    ux: float,
    uy: float,
    uz: float,
) -> None: ...
def setFrustum(self, index: int, left: float, right: float, bottom: float, top: float) -> None: ...
def setFrustumCulling(self, switch: int) -> None: ...
def setGenlocking(self, state: bool) -> None: ...
def setGradientBackground(self, index: int, colors: list, ints: list) -> None: ...
def setGrainSize(self) -> None: ...
def setHighQualityAntialiasing(self, state: bool) -> None: ...
def setIndirectRendering(self, state: int) -> None: ...
def setInteractionMode(self, mode: int) -> None: ...
def setIsolateView(self, index: int, roots: list) -> None: ...
def setKeepRaytracingStructure(self, switch: int) -> None: ...
def setLightmapGPUTextureCompression(self, on: bool) -> None: ...
def setLocalLights(self, switch: int) -> None: ...
def setMono(self, index: int, state: bool) -> None: ...
def setMotionFactor(self, factor: float) -> None: ...
def setNavMode(self, mode: int) -> None: ...
def setNavOrbitMode(self, enabled: bool) -> None: ...
def setNavigationSpeedMode(self, mode: int) -> None: ...
def setNear(self, near: float) -> None: ...
def setNodeMaterial(self, node: NodePtr, mat: MaterialPtr) -> None: ...
def setOcclusionCulling(self, switch: int) -> None: ...
def setOcclusionCullingMode(self, mode: int) -> None: ...
def setOculusRiftHmdCaps(self) -> None: ...
def setOculusRiftTracking(self, s: bool) -> None: ...
def setOculusRiftTrackingOrigin(self, position: Pnt3f) -> None: ...
def setOculusRiftTrackingOriginType(self, originType: int) -> None: ...
def setOpenGLDebugging(self, s: bool) -> None: ...
def setPanningSpeed(self, scalefactor: float) -> None: ...
def setPivot(self, index: int, point: Pnt3f, x: float, y: float, z: float) -> None: ...
def setPostprocessAntialiasingMode(self, on: int) -> None: ...
def setPowerwallWindow(self) -> None: ...
def setPrecomputedRendering(self, state: int) -> None: ...
def setRaytracingDownscaleFactor(self, factor: int) -> None: ...
def setRealisticRendering(self, state: int) -> None: ...
def setRenderFullscreen(self, state: bool) -> None: ...
def setRenderQuality(self, quality: int) -> None: ...
def setRenderRegion(self, on: bool, startX: int, startY: int, endX: int, endY: int) -> None: ...
def setRenderRoot(self, index: int, root: NodePtr) -> None: ...
def setRenderRoots(self, index: int, roots: Any) -> None: ...
def setRenderWindowDocked(self, index: int, state: bool, flags: int) -> None: ...
def setRoll(self, index: int, roll: float) -> None: ...
def setSAAWindow(self, id: int) -> None: ...
def setScreenspaceAO(self, state: int) -> None: ...
def setSelectionMode(self, mode: int) -> None: ...
def setSeparateBakeColor(self, color: Color3f) -> None: ...
def setSeparateBakeIntensity(self, intensity: float) -> None: ...
def setShadeTileSize(self) -> None: ...
def setShadow(self, switch: int) -> None: ...
def setShadowMapUpdates(self, on: bool) -> None: ...
def setShowABSides(self, showASides: bool, showBSides: bool) -> None: ...
def setSnapshotFrame(self, state: bool, width: int, height: int) -> None: ...
def setSortTrans(self, switch: int) -> None: ...
def setSpaceMouseHeight(self, height: float) -> None: ...
def setSpaceMousePivotMode(self, i: int) -> None: ...
def setSpaceMouseTwoAxis(self, s: bool) -> None: ...
def setSpaceMouseViewMode(self, i: int) -> None: ...
def setSpecTexLighting(self) -> None: ...
def setStillDOF(self, state: bool, radius: float, focaldistance: float) -> None: ...
def setSuperSampling(self, state: bool) -> None: ...
def setSuperSamplingOnCameraMovement(self, state: bool) -> None: ...
def setSuperSamplingQuality(self, quality: int) -> None: ...
def setTextureCompression(self, switch: int) -> None: ...
def setTransformNodeSelectionPressed(self, node: NodePtr) -> None: ...
def setTransformNodeSelectionReleased(self, node: NodePtr) -> None: ...
def setTwoSidedLighting(self) -> None: ...
def setUp(self, index: int, vector: Vec3f, x: float, y: float, z: float) -> None: ...
def setUseBake(self, bakeComponent: int, state: int) -> None: ...
def setUseBindless(self, bindlessEnable: bool) -> None: ...
def setUseCommandList(self, commandlistEnable: bool) -> None: ...
def setUseLastDrawTree(self, s: bool) -> None: ...
def setUseMulticastSLI(self, multicastEnable: bool) -> None: ...
def setUsePivotBasedPanning(self, on: bool) -> None: ...
def setUseSinglePassStereo(self, on: bool) -> None: ...
def setUseSpaceMouseHeight(self, value: bool) -> None: ...
def setUseVariableRateShading(self, state: bool) -> None: ...
def setUserMatrix(self, id: int, matrix: Any) -> None: ...
def setVSyncInterval(self, interval: int) -> None: ...
def setVariableRateShadingMode(self, mode: int) -> None: ...
def setVariableRateShadingQuality(self, quality: int) -> None: ...
def setViewportCamera(self, index: int, cameraNode: vrNodePtr) -> None: ...
def setVolumeDrawing(self, switch: int) -> None: ...
def setWireframe(self, switch: int) -> None: ...
def setWireframeSelection(self, switch: int) -> None: ...
def setZWriteTrans(self, switch: int) -> None: ...
def setZeroParallaxDistance(self, zp: float) -> None: ...
def showADSKLogo(self, state: bool) -> None: ...
def showBanner(self, text: str, t: float, bcolor: int, width: int, height: int) -> None: ...
def showCoordinateSystem(self, switch: int) -> None: ...
def showInitialView(self) -> None: ...
def showOculusRiftPerformanceHUD(self, mode: int) -> None: ...
def showPIVRLogo(self, state: bool) -> None: ...
def showProgressCursor(self, s: bool) -> None: ...
def showStatistic(self, switch: int) -> None: ...
def showVRECLogo(self, state: bool) -> None: ...
def showViewCube(self, s: bool) -> None: ...
def showWholeScene(self) -> None: ...
def startStatisticsRecording(self, index: int) -> None: ...
def stopStatisticsRecording(self, index: int) -> None: ...
def subRenderOverlay(self) -> None: ...
def toggleFullscreen(self, index: int, multiDisplayFullscreen: bool) -> None: ...
def toggleRaytracing(self, state: bool) -> None: ...
def updateAllMGLW(self) -> None: ...
def updateAllMGLWAll(self) -> None: ...
def writeRecordedStatistics(self, index: int, path: str) -> None: ...
def zoomTo(self) -> None: ...
