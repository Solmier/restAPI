const e = require('express')
const express = require('express')

const music = require('./music')



const app = express()
app.use(express.json())

app.listen(3000, ()=>{
    console.log('Listening On Port 3000');
})



app.get('/' , (req, res)=>{
    res.json({message : "api is working"})
})

app.get('/api/music' , (req, res)=>{
    res.json(music)
})

app.post('/api/music' , (req, res)=>{

    if(!req.body.date){
        res.status(400)
        return res.json({error: "date is required"})
    }

    const user = {
        id: music.length+1,
        group: req.body.group,
        song : req.body.song,
        date: req.body.date
    }
    music.push(user)
    res.json(user)
})

app.put('/api/music/:id', (req, res)=>{
    let id = req.params.id
    let group = req.body.group
    let song = req.body.song
    let date = req.body.date
    
    let index = music.findIndex((song)=>{
        return(song.id==Number.parseInt(id))
    })

    console.log(id, req.body, index);

    if(index >= 0){
        let sng = music[index]
        sng.song = song
        sng.group = group
        sng.date = date
        res.json(sng)
    }
    else{
        res.status(404)
    }    
})

app.delete("/api/music/:id", (req , res)=>{
    let id = req.params.id;
    let index = music.findIndex((song)=>{
        return(song.id==Number.parseInt(id))
    })
    if(index >= 0){
        let sng = music[index]
        music.splice(index,1)
        res.json(sng)
    }
    else{
        res.status(404)
        res.end()
    }    
})