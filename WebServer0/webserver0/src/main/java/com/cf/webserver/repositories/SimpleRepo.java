package com.cf.webserver.repositories;

import com.cf.webserver.entities.AthleteEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface SimpleRepo extends JpaRepository<AthleteEntity, Long> {

}
