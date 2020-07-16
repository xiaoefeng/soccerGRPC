const Koa = require('koa')
const app = new Koa();
const Router =require('koa-router');
const routers = new Router()
const KoaBodyParser =require('koa-bodyparser');
const Parameter = require('koa-parameter');
const error =require('koa-json-error')
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
    'Goal.proto',
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    });

app.use(Parameter(app));
app.use(KoaBodyParser())
routers.post('/test',async (ctx)=>{
    const {playerID} = ctx.request.body
    const reply =main(playerID);

})
app.use(routers.routes())
.use(routers.allowedMethods())
app.listen(8080,()=>{
    console.log('服务器在8080端口启动')
})
const goal_proto = grpc.loadPackageDefinition(packageDefinition).test;

function main(playerID){
    const client = new goal_proto.Goal('0.0.0.0:2000',
        grpc.credentials.createInsecure());
   const a= client.GoalLys({ playerID }, (err, res)=> {
        console.log(res.result);
        if(err){
            console.log(err)
        }
        
    });
    console.log(a)
}

