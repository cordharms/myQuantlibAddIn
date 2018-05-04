/* -*- mode: c++; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- */

/*
 Copyright (C) 2010 Sebastian Schlenkrich

 */


#include <qlo/templatelocalcorrelation.hpp>


namespace QuantLibAddin {

	LocalCorrelationBSModel::LocalCorrelationBSModel(
		const boost::shared_ptr<ObjectHandler::ValueObject>&                            properties,
		const QuantLib::Handle<QuantLib::YieldTermStructure>&							termStructure,
		const std::vector<std::string>&                                                 aliases,
		const std::vector<boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>>& processes,
		const QuantLib::Handle<QuantLib::LocalCorrTermStructure>&						localCorrTermStructure,
		bool                                                                            permanent)
		: MultiAssetBSModel(properties, permanent) {
		libraryObject_ = boost::shared_ptr<QuantLib::RealStochasticProcess>(
			new QuantLib::LocalCorrelationBSModel(termStructure, aliases, processes, localCorrTermStructure));
	}

	//LocalCorrTermStructure::LocalCorrTermStructure(
	//	const boost::shared_ptr<ObjectHandler::ValueObject>&                            properties,
	//	const std::vector<boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>>& processes,
	//	const boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>&				processToCal,
	//	bool                                                                            permanent) 
	//	: CorrelationTermStructureStrike(properties, permanent) {
	//	libraryObject_ = boost::shared_ptr<QuantLib::LocalCorrTermStructure>(processes, processToCal);
	//}

	CTSlocalInCrossCorrelationFX::CTSlocalInCrossCorrelationFX(
		const boost::shared_ptr<ObjectHandler::ValueObject>&                            properties,
		const std::vector<boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>>& processes,
		const boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>&				processToCal,
		bool                                                                            permanent)
		: LocalCorrSurfaceABFFX(properties, permanent) {
		libraryObject_ = boost::shared_ptr<QuantLib::LocalCorrTermStructure>(
			new QuantLib::CTSlocalInCrossCorrelationFX(processes, processToCal));
	}
	CTSlocalInCrossCovarianceFX::CTSlocalInCrossCovarianceFX(
		const boost::shared_ptr<ObjectHandler::ValueObject>&                            properties,
		const std::vector<boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>>& processes,
		const boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>&				processToCal,
		bool                                                                            permanent)
		: LocalCorrSurfaceABFFX(properties, permanent) {
		libraryObject_ = boost::shared_ptr<QuantLib::LocalCorrTermStructure>(
			new QuantLib::CTSlocalInCrossCovarianceFX(processes, processToCal));
	}
	CTSlocalInCrossNegSkewFX::CTSlocalInCrossNegSkewFX(
		const boost::shared_ptr<ObjectHandler::ValueObject>&                            properties,
		const std::vector<boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>>& processes,
		const boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>&				processToCal,
		double																			beta,
		bool                                                                            permanent)
		: LocalCorrSurfaceABFFX(properties, permanent) {
		libraryObject_ = boost::shared_ptr<QuantLib::LocalCorrTermStructure>(
			new QuantLib::CTSlocalInCrossNegSkewFX(processes, processToCal,beta));
	}
	CTSlocalInCrossVolatilityFX::CTSlocalInCrossVolatilityFX(
		const boost::shared_ptr<ObjectHandler::ValueObject>&                            properties,
		const std::vector<boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>>& processes,
		const boost::shared_ptr<QuantLib::GeneralizedBlackScholesProcess>&				processToCal,
		bool                                                                            permanent)
		: LocalCorrSurfaceABFFX(properties, permanent) {
		libraryObject_ = boost::shared_ptr<QuantLib::LocalCorrTermStructure>(
			new QuantLib::CTSlocalInCrossVolatilityFX(processes, processToCal));
	}
}



