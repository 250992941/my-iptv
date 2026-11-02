import os
import urllib.request
import ssl
import base64
import socket

def main():
    source_url = os.environ.get("SOURCE_M3U_URL")
    target_domain = os.environ.get("TARGET_PROXY_DOMAIN", "caonima.898757.xyz")
    
    # 固定的核心节点参数，直接由代码执行底层拼接，绝不给 Python 产生任何解析歧义的机会！
    proxy_host = "://oshuawei.com"
    proxy_port = 443
    proxy_user = "8cdb3920-978c-68f4-3d9a-0a41cbaeaaa5"
    proxy_pass = "8cdb3920-978c-68f4-3d9a-0a41cbaeaaa5"

    if not source_url:
        raise Exception("致命错误: 未在 GitHub Secrets 中配置 SOURCE_M3U_URL")

    print("==================================================")
    print(f"正在配置标准全局 HTTPS 代理网关（德国节点）...")
    print(f"目标代理服务器域名: {proxy_host}")
    
    # 核心修复：由脚本在微软云机房环境动态解析该长域名的真实 IP，彻底根除本地查不出 IP 的困局
    try:
        print("正在利用 GitHub 骨干网络解析节点 IP...")
        proxy_ip = socket.gethostbyname(proxy_host)
        print(f"解析成功！当前德国节点公网实际物理 IP 为: {proxy_ip}")
    except Exception as dns_err:
        raise Exception(f"致命错误：GitHub 虚拟环境在解析该节点域名时失败。原因: {dns_err}。这说明该域名可能是国内局域网专用专线，海外公网 DNS 无法解析。")

    # 1. 手动将账号密码转换为标准 HTTP 代理所需的 Base64 密文凭证
    auth_str = f"{proxy_user}:{proxy_pass}"
    auth_encoded = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
    
    # 2. 绕过 urllib 的格式化缺陷，直接用解析出来的纯 IP 建立标准的 HTTPS 隧道
    proxy_address = f"https://{proxy_ip}:{proxy_port}"
    proxy_handler = urllib.request.ProxyHandler({
        'http': proxy_address,
        'https': proxy_address
    })
    
    ssl_context = ssl._create_unverified_context()
    opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPSHandler(context=ssl_context))
    
    # 3. 完美注入海外普通 Chrome 浏览器全套标准指纹 + 代理授权凭证 (Proxy-Authorization)
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'),
        ('Accept-Language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7'),
        ('Proxy-Authorization', f"Basic {auth_encoded}"),
        ('Proxy-Connection', 'keep-alive'),
        ('Connection', 'keep-alive')
    ]
    urllib.request.install_opener(opener)

    print("--------------------------------------------------")
    print("正在通过德国加密隧道，直接跨境抓取原 IPTV 服务器的播放列表...")
    
    with urllib.request.urlopen(source_url, timeout=50) as response:
        m3u_content = response.read().decode('utf-8')
        print(f"【大获成功】原始播放列表成功拉回！数据体积: {len(m3u_content)} 字节")

    print("--------------------------------------------------")
    print(f"正在全自动执行国内地址重写和清洗逻辑...")
    original_domain = "caonima.898757.xyz"
    rewritten_content = m3u_content.replace(f"http://{original_domain}", f"https://{target_domain}")
    rewritten_content = rewritten_content.replace(f"https://{original_domain}", f"https://{target_domain}")

    output_path = "live.m3u"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten_content)
    
    print(f"静态转换成功，已物理生成本地文件: {output_path}")
    print("==================================================")

if __name__ == "__main__":
    main()
