#ifndef DATAFORMATS_TRAJECTORYSEED_TRAJECTORYSEED_h
#define DATAFORMATS_TRAJECTORYSEED_TRAJECTORYSEED_h

#include "DataFormats/TrajectorySeed/interface/BasicTrajectorySeed.h"
#include <utility>
/**
   TrajectorySeed contains
   - a TSOS
   - a vector of RecHits (with Own_vector to store polimorphic)
   - a propagation direction
**/
class TrajectorySeed : public BasicTrajectorySeed {
 public:
  TrajectorySeed(){}
  virtual ~TrajectorySeed(){}

  TrajectorySeed(PTrajectoryStateOnDet ptsos, recHitContainer rh, PropagationDirection dir) : hits_(rh), 
    tsos_(ptsos), dir_(dir) {}
  
  range recHits() const {
    return std::make_pair(hits_.begin(), hits_.end());
  }
  unsigned int nHits() const {return hits_.size();}
  PropagationDirection direction() const {return  dir_;}
  PTrajectoryStateOnDet startingState() const {return tsos_;}

  virtual TrajectorySeed * clone() const {return new TrajectorySeed( * this); }

 
 private:
  edm::OwnVector<TrackingRecHit> hits_;
  PTrajectoryStateOnDet tsos_;
  PropagationDirection dir_;
};

#endif
