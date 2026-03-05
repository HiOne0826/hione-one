// GitHub Webhook 接收器
// 用于自动部署 hione.one

const http = require('http');
const crypto = require('crypto');
const { exec } = require('child_process');

// 配置
const PORT = 3000;
const SECRET = 'your-webhook-secret-here'; // 请替换为你自己的密钥
const DEPLOY_SCRIPT = '/root/hione-one/deploy.sh';

// 验证 GitHub Webhook 签名
function verifySignature(body, signature) {
  if (!signature) return false;
  const hmac = crypto.createHmac('sha256', SECRET);
  const digest = 'sha256=' + hmac.update(body).digest('hex');
  return crypto.timingSafeEqual(Buffer.from(digest), Buffer.from(signature));
}

// 执行部署
function runDeploy() {
  console.log('========== 触发部署 ==========');
  console.log(new Date().toISOString());

  exec(`bash ${DEPLOY_SCRIPT}`, (error, stdout, stderr) => {
    if (error) {
      console.error('部署失败:', error);
      console.error('stderr:', stderr);
      return;
    }
    console.log('部署成功！');
    console.log('stdout:', stdout);
  });
}

// 创建 HTTP 服务器
const server = http.createServer((req, res) => {
  if (req.method !== 'POST' || req.url !== '/webhook') {
    res.writeHead(404);
    res.end('Not Found');
    return;
  }

  let body = '';
  req.on('data', chunk => {
    body += chunk.toString();
  });

  req.on('end', () => {
    // 验证签名
    const signature = req.headers['x-hub-signature-256'];
    if (!verifySignature(body, signature)) {
      console.log('签名验证失败');
      res.writeHead(403);
      res.end('Invalid signature');
      return;
    }

    // 检查是否是 push 到 main 分支
    const event = req.headers['x-github-event'];
    if (event === 'push') {
      const payload = JSON.parse(body);
      if (payload.ref === 'refs/heads/main') {
        console.log('收到 main 分支的 push 事件');
        res.writeHead(200);
        res.end('Deploy triggered');
        
        // 异步执行部署
        setTimeout(runDeploy, 1000);
        return;
      }
    }

    res.writeHead(200);
    res.end('OK');
  });
});

server.listen(PORT, () => {
  console.log(`Webhook 服务器运行在 http://0.0.0.0:${PORT}`);
  console.log(`Webhook URL: http://your-server-ip:${PORT}/webhook`);
});
