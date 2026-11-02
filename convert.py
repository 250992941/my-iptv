import os
import urllib.request

def main():
    source_url = os.environ.get("SOURCE_M3U_URL")
    target_domain = os.environ.get("TARGET_PROXY_DOMAIN")
    
    if not source_url:
        raise Exception("错误: 未在 GitHub Secrets 中配置 SOURCE_M3U_URL")

    print(f"正在通过系统底层全局安全网关发起对原始 M3U 的高匿名伪装抓取: {source_url}")
    
    # 模拟最新版普通海外 Chrome 浏览器的完整标准头部
    req = urllib.request.Request(
        source_url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache'
        }
    )

    # 取消普通的 try...except 容错，直接让异常抛出到 GitHub Actions 日志中
    with urllib.request.urlopen(req, timeout=30) as response:
        m3u_content = response.read().decode('utf-8')
        print(f"【成功】原始播放列表数据抓取成功！数据大小: {len(m3u_content)} 字节")

    print(f"开始清洗流媒体地址并将其重写为你的目标路径: {target_domain}")
    original_domain = "caonima.898757.xyz"
    rewritten_content = m3u_content.replace(f"http://{original_domain}", f"https://{target_domain}")
    rewritten_content = rewritten_content.replace(f"https://{original_domain}", f"https://{target_domain}")

    output_path = "live.m3u"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten_content)
    
    print(f"静态转换成功，已成功写入本地文件: {output_path}")

if __name__ == "__main__":
    main()
