const Koa = require('koa')
const app = new Koa();
const   cors = require("koa2-cors")
const Router = require('koa-router');
const routers = new Router()
const KoaBodyParser = require('koa-bodyparser');
const Parameter = require('koa-parameter');
const { Client } = require('groa');
const client = new Client('0.0.0.0', 2000);//连接服务器
app.use(cors())
app.use(Parameter(app));
app.use(KoaBodyParser())
//routers.get('/index.html',function(req, res) {
    //res.sendFile(__dirname+"/"+"index.html");
//})
routers.post('/test', async (ctx) => {
    const { playerID } = ctx.request.body
    await client.loadProto('/home/rlf/project/1/rest/Goal.proto');//先开始加载protobuf
    // Get service defnined
    let Goal = client.getService('test.Goal');//连接hello服务

    // call
    let ret = await Goal.goalLys({
        playerID:playerID
    });//注意服务需要小写首字母（这是服务中的rpc）
    ctx.body = ret.result

})
app.use(routers.routes())
    .use(routers.allowedMethods())
app.listen(3001, () => {
    console.log('服务器在3001端口启动')
})
