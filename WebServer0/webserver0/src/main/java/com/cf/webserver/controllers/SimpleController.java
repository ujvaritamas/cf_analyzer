package com.cf.webserver.controllers;

import com.cf.webserver.entities.AthleteEntity;
import com.cf.webserver.services.SimpleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.Optional;

@RestController
public class SimpleController {

    private SimpleService simpleService;

    @Autowired
    public SimpleController(SimpleService simpleService) {
        this.simpleService = simpleService;
    }

    @GetMapping(path = "/hello")
    public String hello(){
        return "hello";
    }

    @GetMapping(path = "/athletes/{id}")
    public String getById(@PathVariable("id") Long id){
        Optional<AthleteEntity> athlete = simpleService.findById(id);
        if(athlete.isEmpty()){
            return "null";
        }
        return athlete.get().toString();
    }

}
