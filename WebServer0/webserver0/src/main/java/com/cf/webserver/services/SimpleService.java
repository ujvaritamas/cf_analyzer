package com.cf.webserver.services;

import com.cf.webserver.entities.AthleteEntity;
import com.cf.webserver.repositories.SimpleRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class SimpleService {

    private final SimpleRepo simpleRepo;

    @Autowired
    public SimpleService(SimpleRepo simpleRepo) {
        this.simpleRepo = simpleRepo;
    }

    public Optional<AthleteEntity> findById(Long id) {
        return simpleRepo.findById(id);
    }

}
