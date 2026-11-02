import os
import urllib.request
import ssl

def main():
    source_url = os.environ.get("SOURCE_M3U_URL")
    target_domain = os.environ.get("TARGET_PROXY_DOMAIN", "caonima.898757.xyz")
    proxy_url = os.environ.get("HTTPS_PROXY_URL")
    
    if not source_url or not proxy_url:
        print("错误: 未在 Secrets 中配置 SOURCE_M3U_URL 或 HTTPS_PROXY_URL")
        return

    print("正在配置标准全局 HTTPS 代理网关（德国节点）...")
    
    # 允许忽略证书校验（防止部分节点在 GitHub 机房环境由于授信引发 SSL 阻断）
    ssl_context = ssl._create_unverified_context()
    
    # 核心无客户端中转：直接将标准的德国 HTTPS 节点注入 Python 的传输层
    proxy_handler = urllib.request.ProxyHandler({
        'http': proxy_url,
        'https': proxy_url
    })
    
    # 构建带有 SSL 忽略和代理链路的高级 opener
    opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPSHandler(context=ssl_context))
    
    # 模拟最新版海外原生普通浏览器指纹，完美欺骗原服务器的 CF 防护
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'),
        ('Accept-Language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7'),
        ('Connection', 'keep-alive')
    ]
    urllib.request.install_opener(opener)

    try:
        print("准备越过 Cloudflare 盾，发起对原始 M3U 的直接抓取...")
        with urllib.request.urlopen(source_url, timeout=45) as response:
            m3u_content = response.read().decode('utf-8')
            print(f"【成功】原始播放列表通过德国代理直接抓取成功！数据大小: {len(m3u_content)} 字节")
    except Exception as e:
        print(f"【失败】抓取过程中遭遇网络或节点认证阻断: {e}")
        return

    print(f"开始清洗流媒体地址并将其重写为目标路径: {target_domain}")
    
    original_domain = "caonima.898757.xyz"
    rewritten_content = m3u_content.replace(f"http://{original_domain}", f"https://{target_domain}")
    rewritten_content = rewritten_content.replace(f"https://{original_domain}", f"https://{target_domain}")

    output_path = "live.m3u"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten_content)
    
    print(f"静态转换成功，已成功生成本地文件: {output_path}")

if __name__ == "__main__":
    main()

