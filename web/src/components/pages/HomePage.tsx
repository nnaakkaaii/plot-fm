import React from "react";
import GenericTemplate from "../templates/GenericTemplate";

const HomePage: React.FC = () => {
    return (
        <GenericTemplate title="DX Simulator">
            <p>DXシミュレーターでは, 企業のDX推進をサポートするための様々なシミュレーション機能が利用できます/DX Simulator provides a variety of simulation functions to support companies' DX promotion.</p>
        </GenericTemplate>
    );
};

export default HomePage;