/* -*- mode: c++; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- */

/*
 Copyright (C) 2015 Sebastian Schlenkrich

*/



#include <qlo/templatequasigaussian.hpp>

namespace QuantLibAddin {

	RealQuasiGaussianModel::RealQuasiGaussianModel(
						   const boost::shared_ptr<ObjectHandler::ValueObject>& properties,
						         const QuantLib::Handle<QuantLib::YieldTermStructure>& hYTS,
		                         // number of yield curve factors (excluding stoch. vol)
		                         size_t                                             d,       // (d+1)-dimensional Brownian motion for [x(t), z(t)]^T
		                         // unique grid for time-dependent parameters
		                         const std::vector<QuantLib::Time>&                 times,   // time-grid of left-constant model parameter values
		                         // time-dependent parameters, left-piecewise constant on times_-grid
		                         const std::vector< std::vector<QuantLib::Real> >&  lambda,  // volatility
		                         const std::vector< std::vector<QuantLib::Real> >&  alpha,   // shift
		                         const std::vector< std::vector<QuantLib::Real> >&  b,       // f-weighting
		                         const std::vector<QuantLib::Real>&                 eta,     // vol-of-vol
		                         // time-homogeneous parameters
		                         const std::vector<QuantLib::Real>&                 delta,   // maturity of benchmark rates f(t,t+delta_i) 		
		                         const std::vector<QuantLib::Real>&                 chi,     // mean reversions
		                         const std::vector< std::vector<QuantLib::Real> >&  Gamma,   // (benchmark rate) correlation matrix
		                         // stochastic volatility process parameters
		                         QuantLib::Real                                     theta,   // mean reversion speed
 				                 const QuantLib::RealStochasticProcess::VolEvolv    volEvolv,
						   bool permanent) : RealStochasticProcess(properties,permanent) {

        libraryObject_ = boost::shared_ptr<QuantLib::RealStochasticProcess>(
			new QuantLib::RealQuasiGaussianModel( hYTS, d, times, lambda, alpha, b, eta, delta, chi, Gamma, theta, volEvolv ));
    }

	RealMCSimulation::RealMCSimulation(
		                      const boost::shared_ptr<ObjectHandler::ValueObject>& properties,
                              const boost::shared_ptr<QuantLib::RealStochasticProcess> process,
			                  const std::vector<QuantLib::Real>&              simTimes,
							  const std::vector<QuantLib::Real>&              obsTimes,
							  size_t                                          nPaths,
							  QuantLib::BigNatural                            seed,
							  bool                                            richardsonExtrapolation,
							  bool                                            timeInterpolation,
							  bool                                            storeBrownians,
							  bool permanent) : TemplateSimulation(properties,permanent) {
        libraryObject_ = boost::shared_ptr<QuantLib::RealMCSimulation>(
			new QuantLib::RealMCSimulation( process, simTimes, obsTimes, nPaths, seed, richardsonExtrapolation, timeInterpolation, storeBrownians ));
	}

	RealMCPayoffPricer::RealMCPayoffPricer(
		                      const boost::shared_ptr<ObjectHandler::ValueObject>&              properties,
			                  const std::vector< boost::shared_ptr<QuantLib::RealMCPayoff> >& payoffs,
							  const boost::shared_ptr<QuantLib::RealMCSimulation>&            simulation,
			                  bool permanent) : RealMCPayoffPricerBase(properties,permanent) {
        libraryObject_ = boost::shared_ptr<QuantLib::RealMCPayoffPricer>(
			new QuantLib::RealMCPayoffPricer( payoffs, simulation ));
	}

	RealMCCash::RealMCCash( const boost::shared_ptr<ObjectHandler::ValueObject>& properties,
			                    const QuantLib::Time  t,
					            const QuantLib::Time  T,
			                    bool permanent) : RealMCPayoff(properties,permanent) {
        libraryObject_ = boost::shared_ptr<QuantLib::RealMCPayoff>(
			new QuantLib::RealMCPayoff::Cash( t, T ));
	}

	RealMCVanillaOption::RealMCVanillaOption( const boost::shared_ptr<ObjectHandler::ValueObject>& properties,
			          const QuantLib::Time  t,
					  const QuantLib::Time  T,
					  const QuantLib::Real  strike,
					  const QuantLib::Real  callOrPut,
			          bool permanent) : RealMCPayoff(properties,permanent) {
        libraryObject_ = boost::shared_ptr<QuantLib::RealMCPayoff>(
			new QuantLib::RealMCPayoff::VanillaOption( t, T, strike, callOrPut ));
	}


	RealMCAnnuity::RealMCAnnuity( 
		                 const boost::shared_ptr<ObjectHandler::ValueObject>& properties,
			             const QuantLib::Time                                 t,
						 const std::vector<QuantLib::Time>&                   payTimes,
						 const std::vector<QuantLib::Real>&                   payWeights,
			             bool permanent) : RealMCPayoff(properties,permanent) {
        libraryObject_ = boost::shared_ptr<QuantLib::RealMCPayoff>(
			new QuantLib::RealMCPayoff::Annuity( t, payTimes, payWeights ));
	}

	RealMCModelSwaption::RealMCModelSwaption(
		                       const boost::shared_ptr<ObjectHandler::ValueObject>& properties,
			                   const QuantLib::Time                                 t,
						       const std::vector<QuantLib::Time>&                   times,
						       const std::vector<QuantLib::Real>&                   payWeights,
							   QuantLib::Real                                       strike,
							   QuantLib::Real                                       payOrRec,
			                   bool permanent) : RealMCPayoff(properties,permanent) {
        libraryObject_ = boost::shared_ptr<QuantLib::RealMCPayoff>(
			new QuantLib::RealMCPayoff::ModelSwaption( t, times, payWeights, strike, payOrRec ));
	}


}
