BOT_NAME = 'capitaliom'

SPIDER_MODULES = ['capitaliom.spiders']
NEWSPIDER_MODULE = 'capitaliom.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'capitaliom.pipelines.CapitaliomPipeline': 100,

}