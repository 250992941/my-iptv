import os
import urllib.request

def main():
    source_url = os.environ.get("SOURCE_M3U_URL")
    target_domain = os.environ.get("TARGET_PROXY_DOMAIN")
    
    if not source_url:
        print("错误: 未配置 SOURCE_M3U_URL")
        return

    print("正在通过系统全局 NaiveProxy 网关抓取原始 M3U 列表中...")
    
    # 带有完备指纹的 Request 请求
    req = urllib.request.Request(
        source_url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7'
        }
    )

    try:
        # urllib 会直接自动遵循系统环境变量中的 ALL_PROXY
        with urllib.request.urlopen(req, timeout=30) as response:
            m3u_content = response.read().decode('utf-8')
            print("原始列表抓取成功！")
    except Exception as e:
        print(f"网络底层抓取发生错误: {e}")
        return

    print(f"开始重写媒体流链接，目标域名: {target_domain}")
    
    original_domain = "caonima.898757.xyz"
    rewritten_content = m3u_content.replace(f"http://{original_domain}", f"https://{target_domain}")
    rewritten_content = rewritten_content.replace(f"https://{original_domain}", f"https://{target_domain}")

    output_path = "live.m3u"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten_content)
    
    print(f"静态转换成功，已生成本地文件: {output_path}")

if __name__ == "__main__":
    main()
