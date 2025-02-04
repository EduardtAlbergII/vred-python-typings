from builtins import NoneType
from vrOSGTypes import Vec3f

__name__: str
__doc__: NoneType
__package__: str
__spec__: ModuleSpec

def __loader__(self) -> None: ...
def addPreset(self, name: str) -> None: ...
def applyPreset(self, name: str) -> None: ...
def clearRenderVariantSetGroups(self) -> None: ...
def disableRaytracingOverrides(self) -> None: ...
def generateRayFile(self, filename: str, numPhotons: int, maxDepth: int) -> None: ...
def getBrdfMode(self) -> int: ...
def getDenoiseAlpha(self) -> bool: ...
def getDenoiseFilter(self) -> int: ...
def getDenoiseFilterThreshold(self) -> float: ...
def getDenoiserModel(self) -> int: ...
def getDenoiserType(self) -> int: ...
def getEnableDenoiseFilter(self) -> bool: ...
def getIlluminant(self) -> int: ...
def getNURBSRaytracing(self) -> bool: ...
def getRaytracingAAImageFilterHeight(self) -> float: ...
def getRaytracingAAImageFilterType(self) -> int: ...
def getRaytracingAAImageFilterWidth(self) -> float: ...
def getRaytracingAAThresholdQuality(self) -> int: ...
def getRaytracingClampValue(self) -> float: ...
def getRaytracingClampingEnable(self) -> bool: ...
def getRaytracingCores(self) -> int: ...
def getRaytracingFinalGatherRadius(self) -> float: ...
def getRaytracingImageSamples(self) -> int: ...
def getRaytracingInteractiveFinalGatherQuality(self) -> int: ...
def getRaytracingInteractiveIBLQuality(self) -> int: ...
def getRaytracingInteractivePhotonCount(self) -> int: ...
def getRaytracingInteractiveQuality(self) -> int: ...
def getRaytracingInteractiveQualityMode(self) -> int: ...
def getRaytracingInteractiveTextureSharpness(self) -> float: ...
def getRaytracingInteractiveTraceDepth(self) -> int: ...
def getRaytracingLightEvaluationThreshold(self) -> float: ...
def getRaytracingMode(self) -> int: ...
def getRaytracingPhotonLookupCount(self) -> int: ...
def getRaytracingPhotonMapFreezeMode(self) -> int: ...
def getRaytracingPhotonMapRefreshMode(self) -> int: ...
def getRaytracingPhotonMode(self) -> int: ...
def getRaytracingPhotonRadius(self) -> float: ...
def getRaytracingSampleOffset(self) -> int: ...
def getRaytracingSamplesThreshold(self) -> int: ...
def getRaytracingStillFrameFinalGatherQuality(self) -> int: ...
def getRaytracingStillFrameIBLQuality(self) -> int: ...
def getRaytracingStillFramePhotonCount(self) -> int: ...
def getRaytracingStillFrameQuality(self) -> int: ...
def getRaytracingStillFrameQualityMode(self) -> int: ...
def getRaytracingStillFrameSupersampling(self) -> int: ...
def getRaytracingStillFrameTextureSharpness(self) -> float: ...
def getRaytracingStillFrameTraceDepth(self) -> int: ...
def getRaytracingUseFinalGatherForGlossy(self) -> bool: ...
def getRaytracingUseHighQualityTextureFiltering(self) -> bool: ...
def getRenderAlpha(self) -> bool: ...
def getRenderAnimation(self) -> bool: ...
def getRenderAnimationClip(self) -> str: ...
def getRenderAnimationClips(self) -> list: ...
def getRenderAnimationFormat(self) -> int: ...
def getRenderAnimationType(self) -> int: ...
def getRenderBackgroundColor(self) -> Vec3f: ...
def getRenderFilename(self) -> str: ...
def getRenderFps(self) -> int: ...
def getRenderFrameStep(self) -> int: ...
def getRenderICCProfile(self) -> int: ...
def getRenderMetaDataFlags(self) -> int: ...
def getRenderOutputFilenames(self) -> list: ...
def getRenderPNGQuality(self) -> int: ...
def getRenderPasses(self) -> list: ...
def getRenderPixelHeight(self) -> float: ...
def getRenderPixelPerInch(self) -> float: ...
def getRenderPixelWidth(self) -> float: ...
def getRenderPremultiply(self) -> bool: ...
def getRenderPrintHeight(self) -> float: ...
def getRenderPrintWidth(self) -> float: ...
def getRenderRegionEndX(self) -> int: ...
def getRenderRegionEndY(self) -> int: ...
def getRenderRegionStartX(self) -> int: ...
def getRenderRegionStartY(self) -> int: ...
def getRenderStartFrame(self) -> int: ...
def getRenderStopFrame(self) -> int: ...
def getRenderSupersampling(self) -> int: ...
def getRenderTimeInSeconds(self) -> int: ...
def getRenderTonemapHDR(self) -> bool: ...
def getRenderUseClipRange(self) -> bool: ...
def getRenderVariantSetGroups(self) -> list: ...
def getRenderVariantSets(self) -> list: ...
def getRenderView(self) -> str: ...
def getSpectralRaytracing(self) -> bool: ...
def getUseInfiniteRenderInViewport(self) -> bool: ...
def getUseRenderPasses(self) -> bool: ...
def getUseRenderRegion(self) -> bool: ...
def getUseRenderTimeLimit(self) -> bool: ...
def getUseRenderVariantSets(self) -> bool: ...
def getUseRenderViewFromVariantSets(self) -> bool: ...
def removeRenderVariantSetGroup(self, groupName: str) -> None: ...
def setActiveGPUMask(self, mask: int) -> None: ...
def setBrdfMode(self, mode: int) -> None: ...
def setDenoiseAlpha(self, denoiseAlpha: bool) -> None: ...
def setDenoiseFilter(self, filterType: int) -> None: ...
def setDenoiseFilterThreshold(self, value: float) -> None: ...
def setDenoiserInput(self, type: int) -> None: ...
def setDenoiserModel(self, model: int) -> None: ...
def setDenoiserType(self, denoiserType: int) -> None: ...
def setEnableDenoiseFilter(self, on: bool) -> None: ...
def setIlluminant(self, illuminant: int) -> None: ...
def setMaxClusterTileSize(self, tilesize: int) -> None: ...
def setNURBSRaytracing(self, on: bool) -> None: ...
def setRaytracingAAAdaptiveSamples(self) -> None: ...
def setRaytracingAAImageFilter(self, id: int, width: float, height: float) -> None: ...
def setRaytracingAAInitialSamples(self) -> None: ...
def setRaytracingAAThreshold(self) -> None: ...
def setRaytracingAAThresholdQuality(self, threshold: int) -> None: ...
def setRaytracingCausticPhotonRadius(self, radius: float) -> None: ...
def setRaytracingClampValue(self, value: float) -> None: ...
def setRaytracingClampingEnable(self, state: bool) -> None: ...
def setRaytracingCores(self, numCores: int) -> None: ...
def setRaytracingDOFEnable(self) -> None: ...
def setRaytracingFinalGatherRadius(self, radius: float) -> None: ...
def setRaytracingFinalGathering(self, quality: int) -> None: ...
def setRaytracingImageSamples(self, samples: int) -> None: ...
def setRaytracingIndirectPhotonRadius(self, radius: float) -> None: ...
def setRaytracingInteractiveFinalGatherQuality(self, quality: int) -> None: ...
def setRaytracingInteractiveIBLQuality(self, quality: int) -> None: ...
def setRaytracingInteractivePhotonCount(self, count: int) -> None: ...
def setRaytracingInteractiveQuality(self, quality: int) -> None: ...
def setRaytracingInteractiveQualityMode(self, mode: int) -> None: ...
def setRaytracingInteractiveTextureSharpness(self, sharpness: float) -> None: ...
def setRaytracingInteractiveTraceDepth(self, depth: int) -> None: ...
def setRaytracingLightEvaluationThreshold(self, threshold: float) -> None: ...
def setRaytracingMode(self, mode: int) -> None: ...
def setRaytracingMotionBlurEnable(self) -> None: ...
def setRaytracingNURBSEpsilon(self, epsilon: float) -> None: ...
def setRaytracingNURBSMaxDepthCurve(self, depth: int) -> None: ...
def setRaytracingNURBSMaxDepthSurface(self, depth: int) -> None: ...
def setRaytracingNURBSMinDepthCurve(self, depth: int) -> None: ...
def setRaytracingNURBSMinDepthSurface(self, depth: int) -> None: ...
def setRaytracingNURBSNewtonEpsilon(self, epsilon: float) -> None: ...
def setRaytracingNURBSThresholdCurve(self, threshold: float) -> None: ...
def setRaytracingNURBSThresholdSurface(self, threshold: float) -> None: ...
def setRaytracingNURBSUsePreclassification(self, enable: bool) -> None: ...
def setRaytracingPhotonLookupCount(self, count: int) -> None: ...
def setRaytracingPhotonMapFreezeMode(self, mode: int) -> None: ...
def setRaytracingPhotonMapRefreshMode(self, mode: int) -> None: ...
def setRaytracingPhotonMode(self, mode: int) -> None: ...
def setRaytracingPhotonRadius(self, radius: float) -> None: ...
def setRaytracingRenderRegion(self, xBegin: float, yBegin: float, xEnd: float, yEnd: float) -> None: ...
def setRaytracingRenderer(self) -> None: ...
def setRaytracingSampleOffset(self, samplingOffset: int) -> None: ...
def setRaytracingSamplesThreshold(self, samples: int) -> None: ...
def setRaytracingStillFrameFinalGatherQuality(self, quality: int) -> None: ...
def setRaytracingStillFrameIBLQuality(self, quality: int) -> None: ...
def setRaytracingStillFramePhotonCount(self, count: int) -> None: ...
def setRaytracingStillFrameQuality(self, quality: int) -> None: ...
def setRaytracingStillFrameQualityMode(self, mode: int) -> None: ...
def setRaytracingStillFrameSupersampling(self, factor: int) -> None: ...
def setRaytracingStillFrameTextureSharpness(self, sharpness: float) -> None: ...
def setRaytracingStillFrameTraceDepth(self, depth: int) -> None: ...
def setRaytracingUseFinalGatherForGlossy(self, enable: bool) -> None: ...
def setRaytracingUseHighQualityTextureFiltering(self, enable: bool) -> None: ...
def setRenderAlpha(self, state: bool) -> None: ...
def setRenderAnimation(self, enable: bool) -> None: ...
def setRenderAnimationClip(self, clipname: str) -> None: ...
def setRenderAnimationFormat(self, format: int) -> None: ...
def setRenderAnimationType(self, type: int) -> None: ...
def setRenderBackgroundColor(self, r: float, g: float, b: float) -> None: ...
def setRenderCurrentView(self) -> None: ...
def setRenderFilename(self, filename: str) -> None: ...
def setRenderFps(self, fps: int) -> None: ...
def setRenderFrameStep(self, frame: int) -> None: ...
def setRenderICCProfile(self, state: int) -> None: ...
def setRenderMetaDataFlags(self, flags: int) -> None: ...
def setRenderPNGQuality(self, quality: int) -> None: ...
def setRenderPasses(self, state: list) -> None: ...
def setRenderPixelResolution(self, pixelWidth: float, pixelHeight: float, pixelsPerInch: float) -> None: ...
def setRenderPremultiply(self, state: bool) -> None: ...
def setRenderPrintResolution(self, printWidth: float, printHeight: float, pixelsPerInch: float) -> None: ...
def setRenderRegionEndX(self, state: int) -> None: ...
def setRenderRegionEndY(self, state: int) -> None: ...
def setRenderRegionStartX(self, state: int) -> None: ...
def setRenderRegionStartY(self, state: int) -> None: ...
def setRenderStartFrame(self, frame: int) -> None: ...
def setRenderStopFrame(self, frame: int) -> None: ...
def setRenderSupersampling(self, state: int) -> None: ...
def setRenderTimeInSeconds(self, timeInSeconds: int) -> None: ...
def setRenderTonemapHDR(self, state: bool) -> None: ...
def setRenderUseClipRange(self, enable: bool) -> None: ...
def setRenderVariantSets(self, groupName: str, variantSetNames: list) -> None: ...
def setRenderView(self, viewName: str) -> None: ...
def setSpectralRaytracing(self, on: bool) -> None: ...
def setUseInfiniteRenderInViewport(self, state: bool) -> None: ...
def setUseRaySplitting(self, on: bool) -> None: ...
def setUseRenderPasses(self, state: bool) -> None: ...
def setUseRenderRegion(self, state: bool) -> None: ...
def setUseRenderTimeLimit(self, state: bool) -> None: ...
def setUseRenderVariantSets(self, enable: bool) -> None: ...
def setUseRenderViewFromVariantSets(self, enable: bool) -> None: ...
def setUseTwoSampleImportanceSampling(self, on: bool) -> None: ...
def startRenderToFile(self, alwaysOverride: bool) -> None: ...
