import asyncio
from crawl4ai import AsyncWebCrawler


def run_async(coro):
    return asyncio.run(coro)

async def crawl_page(url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return result.markdown if result.success else f"Error: {result.error_message}"


def main():
    print("🌐 Crawl4AI Web Crawler")
    url = input("Enter the URL to crawl: ")

    if url:
        print(f"Crawling {url}...")
        markdown = run_async(crawl_page(url))

        print("\nCrawled Markdown:")
        print(markdown)
    else:
        print("No URL entered!")


if __name__ == "__main__":
    main()
